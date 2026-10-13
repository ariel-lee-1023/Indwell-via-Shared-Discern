"""Check audit coverage and runtime correspondence, not the truth of source interpretations.
Usage: python3 fidelity-ledger/validate-source-audit.py [repository-root]
"""
import hashlib,json,re,sys
from pathlib import Path
root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
ledger=root/'fidelity-ledger'
records=json.loads((ledger/'original-english-claim-audit.json').read_text())
spans=json.loads((ledger/'original-english-reading-spans.json').read_text())
read={(x['source'],x['pdf_page']) for x in spans};errors=[]
files=[root/'SKILL.md',*sorted((root/'references').glob('*.md'))]
covered={str(p.relative_to(root)):set() for p in files}
for rec in records:
 text=(root/rec['file']).read_text();unit=rec['final_text']
 if unit not in text:errors.append(rec['id']+': final text missing');continue
 line=text[:text.index(unit)].count('\n')+1
 if line!=rec['final_line']:errors.append(rec['id']+': final line mismatch')
 covered[rec['file']].update(range(line,line+len(unit.splitlines())))
 for evidence in rec['english_evidence']:
  for page in evidence['pdf_pages']:
   if (evidence['source'],page) not in read:errors.append(rec['id']+': missing reading span')
for p in files:
 rel=str(p.relative_to(root))
 for n,line in enumerate(p.read_text().splitlines(),1):
  if not line.strip() or line.startswith('#') or line=='---' or re.fullmatch(r'[| :\-]+',line) or line.startswith('**Sections**:'):continue
  if n not in covered[rel]:errors.append(f'{rel}:{n}: not inventoried')
report={'status':'pass' if not errors else 'fail','errors':errors,'inventoried_units':len(records),'distinct_pdf_pages_with_spans':len(read),'not_claimed':['all pages read in full','fresh STE verification','independent interpretation review','AI teaching efficacy'],'runtime_sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
(ledger/'original-english-audit-validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='runtime_sha256'},indent=2));sys.exit(bool(errors))
