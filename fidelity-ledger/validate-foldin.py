"""Validate this existing-skill fold-in while retaining the inherited examples directory.
Usage: python3 validate-foldin.py TOOL_ROOT SKILL_ROOT
Retains raw default validator output and exempts only documented shape differences.
"""
import sys,json,re,hashlib
from pathlib import Path
from urllib.parse import unquote
root=Path(sys.argv[2]).resolve();sys.path.insert(0,str(Path(sys.argv[1])/'tools'))
from validate_library import validate
from count_tokens import estimate_tokens,strip_frontmatter
from reference_budget import reference_budget
rep=validate(root,layout='published-repo')
(root/'fidelity-ledger/generic-validation.json').write_text(json.dumps(rep.__dict__,ensure_ascii=False,indent=2))
refs=sorted((root/'references').glob('reference-*.md'))
allowed={'examples/ — the only subdirectory the generated skill may have is references/ (no chapters/, no per-book folders)'}
errors=[e for e in rep.errors if e not in allowed]
sections=[9,7,8,46,16];budgets={}
for p,n in zip(refs,sections):
 text=p.read_text()
 if not re.search(r'PDF|L\d+|p\d+',text):errors.append(f'{p.name}: missing source locators')
 tokens=estimate_tokens(text);target=reference_budget(n,'study','text')
 budgets[p.name]={'sections':n,'tokens_estimated':tokens,'type':'text','depth':'study','target':target,'hard_cap':14000}
 if tokens>14000:errors.append(f'{p.name}: hard cap exceeded')
for p in [root/'SKILL.md',root/'README.md',*root.glob('references/*.md'),*root.glob('examples/*.md'),*root.glob('fidelity-ledger/*.md')]:
 for _,target in re.findall(r'\[([^\]]*)\]\(([^)]+)\)',p.read_text()):
  if re.match(r'^[a-z]+://',target) or target.startswith('#'):continue
  clean=unquote(target.split('#')[0].strip('<>'))
  if clean and not (p.parent/clean).exists():errors.append(f'{p.relative_to(root)}: broken link {target}')
if len(refs)!=5:errors.append('expected exactly five book references')
if (root/'references/acceptance-cases.md').exists():errors.append('acceptance ledger inside runtime references')
for p in [root/'SKILL.md',*sorted(root.glob('references/*.md'))]:
 if re.search(r'[\u3400-\u9fff]',p.read_text()):errors.append(f'{p.name}: non-English CJK text remains')
if 'Respond in the language the user uses, or in the language they explicitly request.' not in (root/'SKILL.md').read_text():errors.append('response language rule missing')
master_tokens=estimate_tokens(strip_frontmatter((root/'SKILL.md').read_text()))
if master_tokens>4500:errors.append('core exceeds cap')
report={'status':'pass' if not errors else 'fail','errors':errors,'profile':'English existing-skill fold-in; inherited examples/STE allowed','generic_shape_exemptions':[e for e in rep.errors if e in allowed],'generic_warnings_preserved':rep.warnings,'core_tokens_estimated':master_tokens,'reference_budgets':budgets,'not_tested':['independent model behavior','learning efficacy','host import','README Mermaid rendering'],'runtime_hashes':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [root/'SKILL.md',*sorted(root.glob('references/*.md')),*sorted(root.glob('examples/*'))]}}
(root/'fidelity-ledger/foldin-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({'status':report['status'],'errors':errors,'core_tokens':master_tokens,'references':budgets},ensure_ascii=False,indent=2));sys.exit(bool(errors))
