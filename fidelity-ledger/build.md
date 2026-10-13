# 构建与版本记录

版本：本地改造候选 2026-10-13；旧版 help-me-understand 保留。任务边界：本地改造与验证，无 commit/push/publication。未来仓库标识为用户指定的 ariel-lee-1023/indwell-via-shared-discern；本次不访问或修改远端。

路径选择依显式交付要求覆盖默认 Git-deliverables 发布路径；先在系统临时目录构建，最终交付到用户指定 AI skills 目录。采用 Books-to-Skill-Refs 的“融入不同结构既有技能”方法，保留 root SKILL.md、references、examples。新增维护资料只入 fidelity-ledger；未改动蒸馏工具代码。增加 README、AGENTS、MIT LICENSE、gitignore 和指向同一规范主体的发现链接，不复制运行资料。

## 预算与实际输出

经核验后的章数为 8、9、7、16、46；模式 text/study。原估输入约1,529,396 tokens 是机器抽取文本粗估，含转换噪声，绝非实际模型阅读量。预算依工具计算：Awareness 7543、Dialogic 7800、Learning 7269、Complex 9300、Multimedia 13473，总45385；主体上限4500；各书text/study硬上限14000。用户以“继续工作”确认后进入生成。

实际输出见[foldin-validation.json](foldin-validation.json)。低于规划目标不以填字数补齐：原技能以轻量、按需参考为约束，保留会改变选择的概念、条件、例外、作者和来源定位，削减重复教学建议、完整课程实施表和未核验效应数字。各书的保留/缩减见 coverage.md。工具按管道表行数自动判定部分文本书为 technical，本次预算仍采用先确认的 text/study，不借更大上限扩容。

## 变更

重写触发与教学立场；按实际表现选择解释、对照、示范、尝试与反馈；按任务路由五书。保留STE、事实精度、箭头语义、计算依据、宿主能力与来源缺口约束。旧来源记录明确标为继承，未伪称本次重查。旧验收案例从运行参考迁至维护账本；增加多轮分支示例和固定条件的交互对照。

## 行为验收诚实性记录

测试集在机器抽取后、实质正文蒸馏与新主体编写前拟定。原JSON的 defined_before_extraction=true 过宽，现更正为 false，并增加 defined_before_semantic_reading=true；不把机器抽取后的规划冒充严格提取前预注册。当前 final 分组在编辑核查中已被查看，因此不得作为未来未经接触的盲测集；后续独立评估应另冻结新场景。

尚无用户选定的独立模型执行端点，未运行三条件预测、实际检索与盲评分；未生成虚假的 acceptance-results.json。本次语义核查不能证明 core gain 或 reference gain，也不证明学习成效。
