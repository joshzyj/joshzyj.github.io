---
title: "Vibe Researching with Coding Agents（中文手册）"
excerpt: "学员实操手册：从一台空白电脑，到一份用编码智能体写成、经过验证、可投稿的论文草稿。"
permalink: /vibe-researching/zh/
author_profile: false
handbook: true
lang: zh
---

{% include handbook-assets.html %}

<p class="hb-backlink" data-hb-lang="zh"><a href="/vibe-researching/">&larr; Vibe Researching 主页</a> &nbsp;·&nbsp; <a href="/vibe-researching/en/">English version</a></p>

{% raw %}
# 如何使用本手册

本手册是两小时工作坊《Vibe Researching with Coding Agents》的学员配套材料。它**不是**讲稿的复刻版，而是一份你可以按自己节奏在自己电脑上完成的实操教程：从“Claude 还没装”开始，到产出一份基于真实 CFPS 数据、经过验证的 Social Forces 风格论文草稿结束。

每一节大致都包含五个固定要素：

1. **目标** — 学完本节你应该能做到什么。
2. **输入什么** — 完整的命令、提示词或代码，统一放在代码块中。如果一行以 `$` 开头，就在终端中输入（不要带 `$`）；如果以 `>` 开头，就在已经启动的 Claude Code 会话中输入。
3. **应该看到什么** — 真实但精简过的终端输出，方便你判断有没有走对。
4. **检查什么** — 智能体跑完后你需要打开并读完的文件。
5. **停一下，自检** — 进入下一节之前你需要回答的问题。

贯穿全书的案例是真实的：基于六波 CFPS 微观数据（2010–2020）写作的 Social Forces 风格论文《中国数字鸿沟》。每一条命令、每一张图、每一个表、每一条验证发现，都来自 2026 年 5 月真实跑过的项目——包括最关键的**七个 CRITICAL 错误**，它们是这门工作坊存在的理由。

手册分为四部分：

- **第一部分：基础（工作坊第一小时）** —— 安装智能体，开启第一个会话，理解项目结构，写出能让智能体执行的提示词，并速览 Claude Code 的新能力 —— 动态工作流、子智能体与自动化（§5A）。
- **第二部分：Open Scholar Skills 全流程（工作坊第二小时）** —— 按你真实使用的顺序串讲所有重点技能，全部以 CFPS 数字鸿沟为载体。
- **第三部分：编排器** —— 当你要写一篇真正认真的论文时（`scholar-full-paper`、`scholar-auto-research`）。
- **第四部分：负责任的实践** —— 自查清单、常见错误、五条原则。

如果你已经在用 Claude 或 Codex，可以略读第一部分，从第 5 节 `scholar-init` 直接开始；如果是零基础，每一步都要做。

# 第一部分：基础

## 1. 什么是“氛围式研究”，以及不是什么

> “AI 一旦碰到你的文件，我们就不再是在随便聊天，而是在设计研究工作流。”

**氛围式研究（Vibe Researching）**是指：在真实研究项目中调用编码型智能体（Claude Code 或 Codex CLI），让它执行有边界的研究任务、留下可检查的产物，而问题、标准、责任始终归你掌握。

**氛围式研究 *不是*：**

- “帮我写一篇关于 X 的论文。”（让智能体同时编造问题、数据和叙述——保证产出漂亮但空心的草稿。）
- “帮我找一个显著结果。”（同时外包假设和证据标准——本质是 p-hacking 的升级版。）
- “听起来挺有道理就直接信。”（流畅的散文不等于已验证的散文。）

**氛围式研究 *是*：**

- “这是允许读取的数据边界，这是要回答的研究困惑，这是证据标准，这是必须产出的产物，这是必须停下来问我的条件。”

### 智能体的三种力量

| 力量 | 含义 | 为什么需要边界 |
|---|---|---|
| **文件** | 能读、能写你指给它的任意文件 | 用得好它最有用；用不好它最危险 |
| **工具** | 能跑 R、Python、shell、git、网络搜索 | 一个错的提示词可能跑出 `rm -rf` |
| **状态** | 能保存日志、跨会话恢复、写项目记忆 | 不留痕迹的状态等于错误的隐身斗篷 |

把权限当作**研究方法**，不是软件设置。智能体的读取边界 = 你的**数据边界**；联网边界 = 你的**隐私边界**；写入边界 = 你的**可复现边界**。

### Claude 与 Codex 的分工

本手册**有意使用两个智能体**，因为我们不希望同一个模型既当作者又当分析者还当审稿人。

- **Claude Code** —— *编排者*。多步骤技能、文字起草、计划模式、项目记忆都很强。我们用它当主流程引擎。
- **Codex CLI** —— *外部审查者*。代码补丁、统计实现、独立审计很强。我们用它做第二把关人。

第一天不必两个都装。先用 Claude。

## 2. 安装 Claude Code 与 Codex

**目标：** 在终端里输入 `claude` 或 `codex` 时能进入一个可用的智能体。

### 2.1 前置依赖

- **macOS、Linux 或 Windows（WSL2）**
- **Node.js ≥ 18**（推荐 20 LTS），用于 Claude Code
- 一个**终端**（Terminal.app、iTerm2 或 Windows Terminal）
- 一个 **Anthropic API key**（或 Claude Pro/Max 订阅）+ 一个 **OpenAI API key**（用于 Codex）
- 可选：**R 4.3+** 与 **Python 3.11+**，因为多数 scholar-skills 在它们上面跑分析

> **Windows 用户请注意：** 本节命令默认你已经在 macOS、Linux 或类 Unix 的 shell 里。如果你用的是 Windows，**不要**直接在 PowerShell 或 `cmd.exe` 里跑这些命令。先翻到 **附录 K —— Windows 安装指引**，按它一步步把 WSL2（Windows Subsystem for Linux）与 Ubuntu 装好。等你在 WSL2 里有了一个能用的 Ubuntu shell，§2 与 §3 的所有命令都能直接照搬，无需修改。每台机器只需要读一次附录 K。

检查 Node 版本：

```bash
$ node --version
v20.11.0
```

如果没有或版本太低，装 [nvm](https://github.com/nvm-sh/nvm) 然后 `nvm install 20`。

> **懒得手动装一堆东西？** 只要 Claude Code 或 Codex 跑起来了（哪怕你机器上只有 Node），就可以让智能体替你安装 Python、R、Git 以及社会科学常用包栈。具体提示词见 §2.6 ——「让智能体替你安装研究工具链」。

### 2.2 安装 Claude Code

```bash
$ npm install -g @anthropic-ai/claude-code
$ claude --version
2.0.x
```

第一次启动会引导你认证：

```bash
$ cd ~/Documents/projects/digital-divide-china-cfps   # 先 cd 进项目目录
$ claude
```

```
 ┌──────────────────────────────────────────────────────┐
 │  Welcome to Claude Code                              │
 │  Choose authentication method:                       │
 │   1) Login with Anthropic Console                    │
 │   2) Use ANTHROPIC_API_KEY                           │
 └──────────────────────────────────────────────────────┘
```

**永远从项目目录里启动 `claude`。** 那个目录就是它的工作根目录，权限边界从此处划定。

### 2.3 安装 Codex CLI

```bash
$ npm install -g @openai/codex
$ codex --version
codex-cli 0.130.0   # 截至 2026-05 的版本，你的可能更新
$ codex login    # 输入 OpenAI API key
```

### 2.3A 桌面 App —— 比 CLI 更友好的另一条路

现在两家都出了**桌面应用**：同一个编码智能体，套在窗口式界面里，让你不碰 `npm`、不开终端也能上手。如果上面的 CLI 安装卡住了 —— 没装 Node、PATH 配不对、公司电脑权限被锁 —— 桌面 App 就是最快把一个能用的智能体摆到你面前的办法。

**目标：** 用对你这台机器最省事的那条路，先让一个能用的 Claude Code 或 Codex 智能体跑起来。

**Claude Code 桌面版（macOS / Windows）。** 从官方页面下载安装包：

- <https://claude.com/download>

桌面版**自带 Claude Code** —— 你**不需要**单独装 Node.js 或 CLI。像装普通应用一样安装（macOS 拖进 Applications；Windows 跑 `.exe`），打开后用你的 Anthropic 账号登录（Pro/Max 订阅，或 Console 登录）。需要 macOS 11（Big Sur）或更高版本。首次上手指引见 <https://code.claude.com/docs/en/desktop-quickstart>。

**Codex App（macOS / Windows）。** 从 OpenAI 官方页面下载：

- <https://developers.openai.com/codex/app>

选 macOS 版本（Apple 芯片或 Intel）或 Windows 版本；Windows 用户也可以在 Microsoft Store 里装。打开后用你的 **ChatGPT 账号**登录（Plus / Pro / Business / Edu / Enterprise 都含 Codex），或填 **OpenAI API key**。这个 App 能并行跑多个 Codex 线程，内置工作树（worktree）、自动化与 Git 支持。

> **你应当看到：** 一个窗口式的智能体，能打开文件夹、读写文件、跑命令、操作 git —— 跟 CLI 一样的能力，只是用按钮代替了敲键。

**让桌面 App 替你把 CLI 装上。** §2.2 里那几条 `npm` 命令，你不必自己敲。桌面 App 打开后，用大白话吩咐它 —— *「在我这台机器上装好 Claude Code CLI，再一步步带我登录」* —— 智能体会检查你的 Node 版本、跑安装程序、修好 `PATH`，最后把一个能用的 `claude` 命令交到你手里。这跟它后面替你搭整套研究工具链（§2.6）是同一个智能体；只不过这次，它先给自己搭好了终端的家。

**…… 但这次工作坊，还是请你把 CLI 也装上、用起来。** 桌面 App 用来「第一次接触」和日常工作都很棒，工作坊之后你尽可以继续用。要你也花十分钟去终端练手，*不是*因为桌面版弱 —— 到现在它也能读你的文件、跑代码、在一次会话里记住上下文、连上 MCP server，跟 CLI 一模一样。真正的理由，是有那么几件事，**图形界面从结构上就做不到**。桌面 App 需要一块屏幕、需要一个人点鼠标；而 CLI 只是文字进、文字出，凡是有 shell 的地方它都能跑：

- **无界面 / 远程。** CLI 能通过 SSH 跑在没接显示器的实验室服务器或 HPC 集群上。当受限数据不能离开一台安全机器时，你是把智能体带到数据跟前 —— 这对一个需要图形桌面会话的窗口 App 来说根本做不到。
- **可脚本化。** `claude -p "……"` 能塞进 shell 脚本、`Makefile` 或 cron 定时任务，于是智能体成了流水线里一个自动化步骤，而不是一个点按钮的人。
- **无人值守、可放大规模。** 用 `tmux`/`nohup` 起的长任务或并行任务，会比你这次会话活得更久 —— 合上笔记本，两百次模型调用照跑一整夜。
- **能和 Unix 组合。** 它的输入输出可以直接用管道、重定向接进 `git`、`grep`、`R`、`awk` —— 无缝落进你本来就在用的科研计算工具链。
- **文字即可复现。** 每一个动作都是一条可记录、可版本管理、可重跑的命令，同事能原样复现你**一模一样**的流程；而点一下鼠标什么痕迹都不留。

还有两条工作坊层面的理由：在 CLI 上学到的一切都能原样搬回桌面 App（反过来则未必）；而且教材都默认终端 —— 插件安装（§2.4）要跑 shell 脚本 `setup.sh`，钩子（§5A）、`.claude/settings.json`、MCP 接线也全是可直接复制粘贴的命令。

所以：如果今天靠桌面 App 才能不卡壳，那很好 —— 用它，或者让它替你把 CLI 装上。但也请让 `claude`（最好连 `codex`）在终端里跑起来，因为从 §2.4 开始，后面都默认你能在 `$` 提示符下敲命令、在会话里用 `>` 发提示词。

### 2.4 安装 `open-scholar-skill` 插件

技能不是 Claude Code 自带的，需要从仓库 clone 下来再跑安装脚本。仓库在 `https://github.com/joshzyj/open-scholar-skill`，里面带 `.claude-plugin/` 清单和一个 `setup.sh` —— 由它把 skills、agents 与 PreToolUse 数据安全 hook 注册进 Claude Code。

装的方式有两种。如果 `git`、SSH 钥匙、shell 脚本对你来说还陌生，用**新手快捷路径**（§2.4.0）—— 让 Claude Code 自己装。如果你想看每一条命令，用 §2.4.1–§2.4.5 的**手动路径**。

#### 2.4.0 新手快捷路径——让 Claude Code 帮你装

装好 Claude Code（§2.2）并在任意目录启动后，把下面这段提示词贴进去：

```
> 请把 open-scholar-skill 插件从
>   https://github.com/joshzyj/open-scholar-skill
> 安装到本机的 Claude Code 里。把它 clone 到
>   ~/.claude/plugins/open-scholar-skill
> 然后运行它的 setup.sh，安装缺失的依赖（git、jq、python3），
> 装完后列出所有 scholar-* 命令做一次验证。
> 任何需要 sudo 或者要写到 ~/.claude 之外的地方，
> 都先停下来问我。
```

Claude 会读 repo 的 README，跑 `git clone`、执行 `setup.sh`、装缺的工具（每一步会向你要权限），装完用 `/help` 自检。任何失败都会把具体报错说出来——你读 transcript，不必背命令。最终状态与手动路径完全一致。

> **新手路径的安全规则**
>
> 1. Claude Code 起在 **`default`** 权限模式（不是 `bypassPermissions`），这样每一步装的时候它仍会问你。Status line 看一眼是不是 `default`，不是的话按 `Shift+Tab` 切换。
> 2. agent 要用 `sudo` 的时候，读清楚它想装什么再点 `y`。插件本身不需要 `sudo`——只在 Linux 上装 `jq` / `python3` 才可能用到。
> 3. agent 报告连不上 `github.com`、或者某个依赖连试三次都装不上，就改走手动路径——这些失败通常需要人去看你本机的 shell、proxy、`PATH`。

Claude 装完后，跳到 §2.4.4 自检一下，再去 §3。

\medskip

#### 2.4.1 前置依赖：git

安装过程依赖 `git`。先确认装了并配置过：

```bash
$ git --version            # 任意 2.x 都行
$ git config --global user.name  "Your Name"
$ git config --global user.email "you@example.com"
```

如果没有 git：

- **macOS：** `xcode-select --install`（Apple 自带 git）或 `brew install git`
- **Ubuntu / Debian / WSL：** `sudo apt install git`

如果以后要 pull 私有仓库，再加一把 SSH key：

```bash
$ ssh-keygen -t ed25519 -C "you@example.com"
$ cat ~/.ssh/id_ed25519.pub
# 把输出粘进 github.com → Settings → SSH and GPG keys
```

#### 2.4.2 安装：clone + 跑 setup

```bash
$ git clone https://github.com/joshzyj/open-scholar-skill.git
$ cd open-scholar-skill
$ bash setup.sh
```

`setup.sh` 会做三件事：

1. 建好 `.claude/skills/` 与 `.claude/agents/` 的内部 symlink。
2. 把 `scripts/gates/pretooluse-data-guard.sh` 注册为 `~/.claude/settings.json` 中的 PreToolUse hook —— 拦截每一次 `Read`、`NotebookRead`、`NotebookEdit`、`Grep`、`Glob`，对 `NEEDS_REVIEW:*` 或 `HALTED` 的文件直接拒绝。
3. 检查 `jq` 与 `python3` 都在；缺任一项 hook 会 fail-closed。

如果 `setup.sh` 报缺依赖，装上（macOS：`brew install jq`；Linux：`sudo apt install jq python3`）再重跑。

#### 2.4.3 以后更新

```bash
$ cd open-scholar-skill
$ git pull
$ bash setup.sh    # 幂等；刷新 symlink 与 hook 注册
```

#### 2.4.4 验证

任意项目目录里启动 Claude Code：

```
> /help
```

应该能看到一长串 `scholar-*` 命令。再做个快速检查：

```
> /scholar-init --help
```

能打印帮助即可进入 §3。

#### 2.4.5 排错

- **`/help` 里看不到 skills** —— symlink 没装好。回到 clone 目录，重跑 `bash setup.sh`，看是否出现 `▸ Checking symlinks...` 段落。
- **PreToolUse hook 拦了一个本不该拦的文件** —— 这是数据安全闸门在工作。用 `/scholar-init review` 解决，**不要**禁用 hook。
- **公司代理后面** —— 用带 token 的 HTTPS：

  ```bash
  $ git clone https://<token>@github.com/joshzyj/open-scholar-skill.git
  ```

  或者下载 ZIP 解压后再跑 `setup.sh`。

## 2.5 让 Claude Code 接入 GLM、DeepSeek 或本地模型

**目标：** 继续使用同一个 Claude Code CLI、同一套 `open-scholar-skill` 插件、同一种项目结构，只是把模型调用切到 Z.ai/GLM、DeepSeek，或者你自己机器上跑的本地模型。

你**不需要**装新的 CLI，也不需要替换脚本，更不应该每次会话前手动改 JSON。Claude Code 只看两个环境变量——`ANTHROPIC_BASE_URL` 和 `ANTHROPIC_AUTH_TOKEN`——只要对方暴露 Anthropic-compatible endpoint，Claude Code 就能直接对话。GLM（Z.ai 国际站和国内 BigModel）以及 DeepSeek 都已经提供这类入口。对**真正本地**的模型（DeepSeek-R1 蒸馏版、Qwen2.5-Coder、Llama、GLM），Claude Code 仍然需要一个 Anthropic-compatible 的前端：Ollama、vLLM、llama.cpp 暴露的都是 OpenAI 风格的接口，所以要在前面加一层小转换层——`claude-code-router` 或 `litellm`——把响应重写成 Anthropic schema。其余流程完全一致。

### 2.5.1 提供商速查表

| 提供商 | Endpoint host | 需要设置的模型 |
| ----- | ------------- | ------------- |
| GLM / Z.ai（国际） | `api.z.ai` | Opus → `glm-5.1`；Sonnet → `glm-5-turbo`；Haiku → `glm-4.5-air`。同时 `API_TIMEOUT_MS=3000000`。 |
| GLM 中国大陆 | `open.bigmodel.cn` | 同样思路；按账号可用的 GLM 系列选择。 |
| DeepSeek | `api.deepseek.com` | Opus / Sonnet → `deepseek-v4-pro`；Haiku 与 subagents → `deepseek-v4-flash`。 |
| 本地 —— Ollama（经 CCR/代理） | CCR → `http://localhost:11434/v1/chat/completions` | 你拉下来的任意 tag（如 `qwen2.5-coder:32b`）；需要一层转换。详见 §2.5.5。 |
| 本地 —— vLLM / llama.cpp（经代理） | 你启动的代理地址 | 由你的代理决定，详见 §2.5.5。 |

完整 `ANTHROPIC_BASE_URL`：Z.ai 为 `https://api.z.ai/api/anthropic`，BigModel 为 `https://open.bigmodel.cn/api/anthropic`，DeepSeek 为 `https://api.deepseek.com/anthropic`。后缀 `/anthropic` 是让 endpoint 走 compatibility shim 的关键，漏掉它是最常见的配置错误。

**模型名变得很快。** 本节里的模型 ID（`glm-5.1`、`glm-5-turbo`、`deepseek-v4-pro` 等）只是示例。开工前先查 provider 当前的模型列表——Z.ai/BigModel 和 DeepSeek 各自都有——用你账号能调用的确切名字；粘一个已下线的 tag，是仅次于漏掉 `/anthropic` 后缀的第二常见错误。

### 2.5.2 方案 A —— 在 `~/.claude/settings.json` 里写死后端

最简单的设置：把 Claude Code 指向一个后端，保存文件，之后每次会话都用它，直到你改回来为止。

**GLM 示例：**

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.z.ai/api/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "your_zai_key",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5.1",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5-turbo",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-4.5-air",
    "API_TIMEOUT_MS": "3000000"
  }
}
```

**DeepSeek 示例：**

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.deepseek.com/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "your_deepseek_key",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "deepseek-v4-pro",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "deepseek-v4-pro",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-flash"
  }
}
```

重启 Claude Code；触发任意一次工具调用或 `/usage`，确认后端已切换。

### 2.5.3 方案 B —— 把 key 放到项目外，用 shell 函数切换

每次工作坊前改 `settings.json` 既痛苦又容易把 key 误推到 git。更好的做法：把所有 provider key 放到 `~/.api-keys`（chmod 600），由 `~/.zshrc` 或 `~/.bashrc` source 进来，再定义几个 shell 函数；每个函数 export 自己那套环境变量，然后启动 `claude`：

```bash
# ~/.api-keys（绝对不要提交到任何仓库）
export ANTHROPIC_API_KEY="sk-ant-..."
export ZAI_API_KEY="..."
export DEEPSEEK_API_KEY="..."

# ~/.zshrc
[ -f ~/.api-keys ] && source ~/.api-keys

glm() {
  export ANTHROPIC_BASE_URL="https://api.z.ai/api/anthropic"
  export ANTHROPIC_AUTH_TOKEN="$ZAI_API_KEY"
  export ANTHROPIC_DEFAULT_SONNET_MODEL="glm-5-turbo"
  export ANTHROPIC_DEFAULT_OPUS_MODEL="glm-5.1"
  export ANTHROPIC_DEFAULT_HAIKU_MODEL="glm-4.5-air"
  export API_TIMEOUT_MS=3000000
  claude "$@"
}

deepseek() {
  export ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
  export ANTHROPIC_AUTH_TOKEN="$DEEPSEEK_API_KEY"
  export ANTHROPIC_DEFAULT_SONNET_MODEL="deepseek-v4-pro"
  export ANTHROPIC_DEFAULT_OPUS_MODEL="deepseek-v4-pro"
  export ANTHROPIC_DEFAULT_HAIKU_MODEL="deepseek-v4-flash"
  claude "$@"
}

claude-anthropic() {
  unset ANTHROPIC_BASE_URL ANTHROPIC_AUTH_TOKEN
  unset ANTHROPIC_DEFAULT_SONNET_MODEL
  unset ANTHROPIC_DEFAULT_OPUS_MODEL
  unset ANTHROPIC_DEFAULT_HAIKU_MODEL
  claude "$@"
}
```

之后 `glm` 在 Z.ai 上启动 Claude Code，`deepseek` 在 DeepSeek 上启动，`claude-anthropic` 回到原版 Anthropic。PATH 里的二进制 `claude` 始终是同一个你信任的 CLI。

### 2.5.4 方案 C —— CC Switch：一键切换 provider 的图形界面

方案 A、B 都要手动改配置。如果你要在多个 provider 或多个账号之间来回切 —— 一个项目用 Anthropic 登录，另一些用 GLM 和 DeepSeek，还有个合作者的仓库用 Kimi key —— 那么用一个替你改这些配置的图形界面会更不容易出错。**CC Switch** 是一个跨平台桌面应用，在一个窗口里管理 Claude Code（以及 Codex、Gemini CLI、Claude Desktop 等）的 provider 配置，内置 50+ provider 预设，还带一个系统托盘菜单可即时切换。它是开源的第三方工具，**不是** Anthropic 官方产品。

**安装。**

```bash
# macOS（Homebrew）—— 已签名并经 Apple 公证
brew install --cask cc-switch

# Linux（Arch）
paru -S cc-switch-bin
```

**Windows** 下载 `.msi` 安装包（Windows 10+）；其它 **Linux** 发行版用 `.deb`、`.rpm` 或通用的 `.AppImage`。所有安装包都在官方发布页：

- 官网：<https://ccswitch.io>
- 下载：<https://github.com/farion1231/cc-switch/releases>

**工作原理。** CC Switch 把你的 provider 定义存在本地 SQLite 数据库 `~/.cc-switch/cc-switch.db` 里；切换时，它把对应的值写进各工具的实时配置 —— 也就是方案 A 里你手动改的那些 `~/.claude/settings.json` 环境变量 —— 采用原子写入，并在 `~/.cc-switch/backups/` 里滚动备份。Claude Code 支持**热切换、无需重启**；其它 CLI 切换后需要重启终端。

**四步：添加与切换。**

1. **Add Provider（添加）** → 选一个预设（Anthropic 官方、GLM/Z.ai、DeepSeek、Kimi/Moonshot ……）或填自定义 base URL + key。
2. 选中该 provider 点 **Enable（启用）** —— 或直接从**托盘**菜单里选，即时切换。
3. 重启终端（Claude Code 不需要），触发任意工具调用或 `/usage` 确认后端已切换。
4. 想切回 Anthropic 登录：启用 **"Official Login"** 预设，重启，再正常登录。

**两条提醒 —— 工作坊的数据边界规则依然适用。**

- **它把你的 API key 明文存**在 `~/.cc-switch/cc-switch.db` 里。把这个文件当凭据库对待：不要放在共用的实验室机器上，不要放进你无法掌控的同步 / 备份目录，永远不要提交进 git。在借来的电脑上，宁可用方案 B（key 放 `~/.api-keys`，`chmod 600`），或用完清理干净。
- **很多预设是社区中转（relay），不是厂商自己的 endpoint。** 中转方能看到你发给它的每一条 prompt —— 包括受访者文本。在把含敏感数据的项目路由到任何非官方后端之前，先做 §2.5.6 的信任检查；受限数据请优先用官方通道或你已核验过的 provider。

CC Switch 不替代方案 A/B —— 它只是把它们收进一个界面。工作流的其它部分（插件、`CLAUDE.md`、权限门）都不变。

### 2.5.5 在本机跑本地模型

如果机构禁止把数据发到云端 API，或者你需要可离线复现的实验，可以在本机跑一个 checkpoint，再把 Claude Code 路由过去。注意：Claude Code 说的是 Anthropic Messages API，而本地服务（Ollama、vLLM、llama.cpp）说的是 OpenAI 风格的 chat completions，所以中间要垫一层薄薄的转换层。`claude-code-router`（CCR）最省事：它对 provider 说的是 OpenAI 风格的 chat completions，所以这三者都当作普通的 OpenAI-compatible 后端接入即可——不需要为每个本地服务单独配 transformer。

**路径 A —— 用 CCR 在前面接住 Ollama（最简单的本地路线）。** Ollama 暴露的是 OpenAI 风格的接口（`/v1/chat/completions`）和它自己的原生 API——不是 Claude Code 期望的 Anthropic `/v1/messages` 格式——所以和 vLLM、llama.cpp 一样，前面要垫一层 shim：

```bash
# 1. 安装 Ollama（macOS / Linux / WSL）
$ curl -fsSL https://ollama.com/install.sh | sh
$ ollama --version

# 2. 按显存 / 内存拉一个本地模型。当前 tag 见
#    https://ollama.com/library ，下面这些现在就有：
$ ollama pull qwen2.5-coder:32b   # 偏代码的强力本地模型
$ ollama pull deepseek-r1:14b     # 蒸馏推理模型
#    GLM 系列也在库里 —— 在该页搜 "glm"。

# 3. 用 CCR 接住 Ollama（CCR 安装见路径 B）。在 ccr ui 里加一个
#    "ollama" provider，base URL 填 http://localhost:11434/v1/chat/completions，模型填你拉的 tag，然后：
$ ccr code
#    会话里：/model ollama,qwen2.5-coder:32b
```

直接把 `ANTHROPIC_BASE_URL` 指到 `http://localhost:11434` 是**不行**的：Claude Code 会去 POST `/v1/messages`，而 Ollama 并不提供这个端点。是这层转换把两种 schema 接起来的。

**路径 B —— `claude-code-router`（CCR），安装与路由。** CCR 既是单个本地模型的 shim（路径 A），也是*混合* provider 的方式——给不同档位走不同路由（Opus 走 Z.ai、Sonnet 走 DeepSeek、Haiku 走本地 Ollama），并可在会话中途用 `/model provider,model` 手动切换（要做故障回退可自己写一段 `router.js` 自定义路由）：

```bash
$ npm install -g @musistudio/claude-code-router
$ ccr ui          # 打开浏览器配置界面，并创建
                  # ~/.claude-code-router/config.json
$ ccr start       # 启动路由服务
$ ccr code        # 通过 CCR 启动 Claude Code
```

没有 `ccr config init` 这个命令；配置文件在你第一次跑 `ccr ui`（或 `ccr start`/`ccr code`）时自动创建，位于 `~/.claude-code-router/config.json`。在那里或用 `ccr ui` 编辑 `default` 与各档位路由，改完跑 `ccr restart` 生效。在 CCR 会话里，`/model deepseek,deepseek-v4-pro` 或 `/model ollama,qwen2.5-coder:32b` 可在对话中途切换路由 —— `provider,model` 这种写法是 CCR 的特性，不是原版 Claude Code 的。

> **vLLM / llama.cpp。** 如果你已经用 vLLM（`vllm serve <model>`）或 llama.cpp（`llama-server`）提供服务，它们暴露的是 OpenAI 风格的 chat completions，不是 Anthropic 风格。vLLM 自带一份 Claude Code 接入指引；否则在前面套一层 `litellm`、`anthropic-proxy` 或 CCR 转换 OpenAI ↔ Anthropic schema 即可。Claude Code 这一侧保持不变。

### 2.5.6 信任新后端前必做的三项检查

Open Scholar 技能**不是 model-agnostic** 的。它们依赖长上下文阅读、tool use 和结构化 JSON 输出。在用非 Anthropic 后端跑 CFPS 流水线之前，必须先过下面三步烟测：

1. **Tool-use round-trip。** 在沙盒项目里说：“读取 `grades.csv`，跑一段 Python 计算平均值，把结果写入 `out.txt`”。如果后端悄悄跳过 `Bash` 调用、自己编造文件内容、或者只用文字给出答案而没有生成 `out.txt`，那么所有依赖产物的 scholar-skill 都会失败。
2. **长 prompt 稳定性。** 粘贴一段 30 页的 CFPS 代码本节选，让 agent 抽出变量名与对应波次。有效上下文窗口偏小的后端会在后面几页静默丢内容。
3. **技能调用。** 跑一遍 `/scholar-init --slug smoke-test` 和 `/scholar-safety scan`。如果模型拒绝调用 skill、返回错误路径、或者“忘记”了 PreToolUse hook，就**不要**用它处理真实数据。

把每一项的结果用一行写到 `logs/backend-test.md`。**不要对外宣称任何模型与 open-scholar-skill 套件“完全兼容”** —— 你只能说：在某月某日跑过烟测，列出的几个 skill 通过。

> **工作坊纪律：** 工作坊现场，一台笔记本只用一个后端。在流水线中途换 provider，是让一篇论文前后两半对同一个 CFPS 变量定义打架的最快方法。

## 2.6 让智能体替你安装研究工具链

**目标：** 只要 `claude`（或 `codex`）能启动，剩下的安装工作 —— Python、R、Git、系统编译工具、社会科学常用包栈（`tidyverse`、`pandas`、`statsmodels`、`scikit-learn` 等）—— 都交给智能体。你只需要逐条审核它给出的命令，逐条点批准，最终在 transcript 里留下一份可在另一台电脑复用的安装日志。

让智能体干这件事有三个好处：它会自动挑对操作系统对应的包管理器（macOS 用 `brew`、Debian/Ubuntu 用 `apt`、Windows 用 `winget` 或 `choco`），它会按正确顺序处理依赖（先系统库，再语言运行时，最后包），并且每条执行过的命令都会留在对话里。

### 2.6.1 开始之前 —— 先把安全规则讲清楚

系统级安装会动到共享状态。**先告诉智能体规矩，再让它动手：**

```
> 请帮我在这台机器上装一套社会科学研究工具链。开始之前，请遵守以下规则：
>
>   1. 先识别系统与包管理器，把结果告诉我；
>   2. 每一条安装命令先告诉我再跑；任何 sudo 命令都必须逐条经我批准；
>   3. 优先用用户级安装方式（rustup、pyenv、rbenv、conda --user、renv、
>      R 用户库），不要去改系统自带的 Python 或 R；
>   4. 每一步装完都跑一次 --version 确认成功，再进下一步；
>   5. 把你执行过的每一条命令追加写入当前目录下 logs/install.md，
>      方便我换台电脑时复用。
>
> 先识别一下我的操作系统、shell，以及 {python3, R, git, make, pandoc,
> quarto, jq} 中哪些已经在 PATH 里。把结果给我，然后等我下一步指示。
```

这一段全程用 **`default`** 权限模式。**不要**切到 `acceptEdits` 或 `bypassPermissions` —— 每一次 `sudo`、`brew install`、`apt install`、`npm install -g` 都应该是一次单独的批准。

### 2.6.2 覆盖 90% 场景的四条提示词

智能体把机器情况摸清楚之后，按顺序发下面四条提示词。每条都足够小，便于你逐条审核。

**(1) Git、SSH 与系统编译工具。**

```
> 请把版本控制与源码编译需要的基础组件装好：
>
>   - git（系统包管理器里的最新稳定版）
>   - 一个 SSH client 和一对 ed25519 key（~/.ssh/id_ed25519）；
>     如果我已经有 key，绝对不要覆盖
>   - GNU make、C/C++ 编译器、pkg-config、curl
>   - jq（open-scholar-skill 的 PreToolUse hook 必须用到）
>
> macOS 走 Homebrew（没装就先装上）。Debian/Ubuntu/WSL 走 sudo apt update
> && sudo apt install。每条命令先给我看再跑。
>
> 装完跑一遍 git --version、make --version、cc --version、jq --version，
> 再 cat ~/.ssh/id_ed25519.pub 把公钥打印出来，我好贴到 GitHub。
```

**(2) Python：`pyenv` + 项目级虚拟环境。**

我们刻意不走 `sudo pip`，也不动系统自带的 Python。用户级 `pyenv` + 项目级 `.venv`，是唯一能在系统升级后仍然不坏的方案。

```
> 帮我装 pyenv（Windows 上用 pyenv-win），用它装 Python 3.11.x 并设为
> 用户默认版本。然后在当前项目目录建一个 .venv，把社会科学标准包栈装进去：
>
>   numpy, pandas, scipy, statsmodels, scikit-learn, matplotlib, seaborn,
>   pyarrow, jupyterlab, ipykernel, linearmodels, pyreadstat, openpyxl,
>   tqdm, requests, beautifulsoup4, lxml, plotnine, great_tables, ruff,
>   black, mypy, pytest
>
> 把版本固定到 requirements.txt。再把这个 venv 注册成名为 "vibe-py311"
> 的 Jupyter kernel。最后打印 python --version、pip list | head 和
> kernel 列表。
```

如果还要做计算社会科学（NLP、嵌入、LLM 标注、网络分析、地理空间），追加一段：

```
> 再装：transformers, sentence-transformers, datasets, accelerate,
> tiktoken, openai, anthropic, spacy, nltk, gensim, networkx, igraph,
> geopandas, shapely, pyproj, rasterio, contextily, folium。
> 没有 NVIDIA GPU 时不要拉 CUDA 版 torch，默认用 CPU wheel。
```

**(3) R + 社会科学包栈。**

R 在各操作系统上的安装路径差异较大，让智能体自己选路线比死记四套命令省事。关键提示词是：「装到用户库里，不要每个包都 sudo。」

```
> 装 R 4.4.x 和 RStudio Desktop（免费版）。macOS 走 CRAN 官方 .pkg；
> Debian/Ubuntu/WSL 走 CRAN apt 源（cran.r-project.org/bin/linux/ubuntu）。
> R 进 PATH 后，在 ~/R/library 建一个用户库（如不存在），在 ~/.Renviron
> 里把 R_LIBS_USER 指过去，然后把以下包装进用户库：
>
>   tidyverse, data.table, lubridate, janitor, haven, readxl, writexl,
>   here, fs, glue, scales, broom, modelsummary, gt, gtsummary, kableExtra,
>   flextable, officer, knitr, rmarkdown, quarto, tinytex,
>   fixest, lme4, sandwich, lmtest, marginaleffects, estimatr, sjPlot,
>   ggplot2, ggdist, ggrepel, patchwork, ggeffects, plotly, DT,
>   survey, srvyr, lavaan, psych, mice, naniar, VIM, future, furrr,
>   renv, usethis, devtools, remotes, languageserver, lintr, styler, testthat
>
> 做计算社会科学的（等我确认后）再加：tidytext, stm, quanteda, text2vec,
> conText, igraph, tidygraph, ggraph, sf, terra, tmap, leaflet, gganimate。
>
> 装完跑 R -e 'sessionInfo()'，把已安装的包列表（含版本号）写到
> logs/r-pkgs.md。
```

**(4) Quarto + 最小 LaTeX，保证 PDF 渲染能跑通。**

很多流水线在最后一步翻车：「论文写完了但渲染不出 PDF。」早一点把这个搞定：

```
> 装 Quarto 最新稳定版，再装一套最小的 TeX。macOS 与 Linux/WSL 上
> 推荐 quarto install tinytex（约 200MB），不要装完整 MacTeX/TeXLive
> （30GB 那种）。装完跑 quarto check，再写一份 10 行的 hello.qmd 渲染
> 成 hello.pdf，确认整条链路通了。
```

### 2.6.3 Codex 风格的提示词

同样的提示词换到 `codex` 上几乎可以照搬，只要在每段最前面加一句 `"在跑每一条命令前先告诉我它是干什么的"` —— Codex 默认解释得偏少。Codex 偏好 `python -m venv`，在干净机器上没问题，但和系统已有 Python 冲突时容易出错；上面 pyenv 那条提示词更稳。

### 2.6.4 把安装日志固化下来

四条提示词都跑完之后，再追加一条：

```
> 把这次会话里的所有安装行为整理成 logs/install.md，按四步分节
> （系统工具 → Python → R → Quarto/LaTeX）。每一步写明确切命令、--version
> 输出，以及一开始检测到的操作系统、shell 和架构。我明天要在另一台
> 笔记本上把这套环境复刻一遍。
```

这份日志就是产物。下次同事问「我该怎么把环境搭起来？」，把 `logs/install.md` 丢给他，让 Claude（或 Codex）在他机器上复跑一遍即可。

### 2.6.5 不要让智能体动的几类东西

少数几类软件最好你自己装，不要交给智能体：

- **系统级数据库**（Postgres、MySQL）—— 太容易覆盖现有实例、清掉本地数据。
- **替换 shell / 终端模拟器** —— 智能体没法重启自己所在的 shell，半路换会出诡异错误。
- **GPU 驱动、CUDA 工具链** —— 牵涉重启与厂商特定决策。
- **任何需要改 `/etc/hosts`、防火墙、VPN 客户端的事**。

除此之外 —— 语言运行时、包、命令行工具、编译依赖、文档工具链 —— 让智能体逐条批准式安装，比你自己装更快、更可复现、还顺手留下了纸面记录。

## 3. 你的第一次智能体会话

**目标：** 60 秒内走完一遍“请求 → 提议 → 批准 → 产物 → 验证”循环。

建一个沙盒：

```bash
$ mkdir -p ~/sandbox-vibe && cd ~/sandbox-vibe
$ printf "subject,score\nAnna,0.81\nBen,0.74\nCara,0.92\n" > grades.csv
$ claude
```

会话里：

```
> 读 grades.csv，告诉我平均分，以及哪些人高于平均分。
```

Claude 会**先**提出工具调用。**先读再批准。** 一个典型界面：

```
 Claude wants to use Read on /Users/you/sandbox-vibe/grades.csv
 ───────────────────────────────────────────────────────────
   path: /Users/you/sandbox-vibe/grades.csv
 ───────────────────────────────────────────────────────────
   [a] approve once   [s] always allow this dir   [n] deny
```

按 `a`。它可能再提议跑一段 Python 或 R，再批准一次。结果：

```
 Mean score: 0.823
 Above mean: Cara (0.92)
```

整个工作坊里所有的 scholar-skill 会话都是这个循环的放大版：

1. **请求** —— 你用自然语言提的需求
2. **提议** —— 智能体打算执行的工具调用
3. **批准 / 拒绝** —— 你的选择
4. **产物** —— 落到磁盘上的文件
5. **验证** —— 你打开文件检查

记住一句话：**屏幕上打印的答案不重要，留在磁盘上的产物和痕迹才重要。**

### 3.1 权限模式——快速入门

Claude Code 共有**六种**权限模式：`default`、`acceptEdits`、`plan`、`auto`、`dontAsk`、`bypassPermissions`。并非每个会话都能用到全部六种：`auto` 需要符合条件的账户和较新的模型，`dontAsk` 只能用 `--permission-mode dontAsk` 设定——用 `/help` 看你装的版本暴露了哪些。新手最常用的两种是：

- **`default`** —— 每个工具 / 路径首次使用都弹出确认。敏感数据、首跑某项目，留在这里。
- **`plan`** —— 只读“探查”模式，智能体必须先写计划，未获批准前不能编辑、不能跑命令。任何破坏性或昂贵的多步操作之前先进。

按 `Shift+Tab` 循环切换 `default → acceptEdits → plan`（账户符合条件时还会进入 `auto`），再按继续循环。完整的六种模式及各自的安全含义见 §3.2：`acceptEdits` 自动通过编辑，`auto` 在后台安全分类器的审查下自动执行一切，`dontAsk` 只允许预先批准的工具，`bypassPermissions` 跳过所有检查。

### 3.2 高频命令

> **关于命令准确性。** 下面的命令对照 Claude Code v2.1.154（与 Opus 4.8 同日发布，2026-05-28）核对。Claude Code 的发布节奏很快——你装的版本可能比本手册更新，或更旧。装好后随时 `/help` 看实时命令列表。"自治与多会话"小节包含 2.x 周期新加的命令，包括 Dynamic Workflows 研究预览（`/workflows`）和后台会话工作链（`claude --bg`、`/resume <bg-id>`）；如果某个命令在你装的版本里识别不出来，就当它还没进你的版本。括号里的第二个名字是别名，效果一致。

#### 项目设置 / 记忆

```
/init                  生成 CLAUDE.md 项目记忆文件
/permissions           查看或调整工具权限
/doctor                环境与配置诊断
/usage   (或 /cost)    显示本会话 token 与美元消耗。
                       v2.1.149+：/usage 现在按 skills、subagents、plugins、
                       MCP servers 分类拆账，便于你在给整条流水线
                       开 /effort xhigh 之前先看哪个 scholar-skill
                       是最大成本项。
/reload-skills         v2.1.152+：扫描 ~/.claude/skills/ 与本项目
                       .claude/skills/ 目录，不用重启会话就能加载新技能。
                       适用：刚改完一个 SKILL.md、或刚拉了一版新的
                       open-scholar-skills。SessionStart hook 可以设
                       "reloadSkills": true，让新技能在本会话内可用。
```

#### 会话控制

```
/compact                          压缩历史以释放上下文
/rewind  (或 /undo)               回滚到更早的检查点
/resume  (或 /continue) [id]      继续上一次会话
/recap                            一句话总结本会话
/rename <name>                    给当前会话起名（之后 /resume <name>）
/clear   (或 /reset, /new)        开新对话（CLAUDE.md 不动）
/exit    (或 /quit)               干净退出
连按 Ctrl+C                       取消当前正在执行的操作
```

#### 移动端 / 远程操控

```
/remote-control  (别名: /rc)   把当前本地会话开放给 claude.ai/code
                                与手机 App。执行仍然在你本机，远端
                                只是同步对话视图。适合：办公室开了
                                一个长流水线，想去咖啡店继续盯。
```

关掉远端标签页**不会**停掉本机会话；除非你在本地 `/exit`，agent 会一直跑。

#### 自治与多会话 —— Claude Code 2.x 新增

下列功能是 Opus 4.6 / 4.7 / 4.8 周期里加进来的，它们改变了研究者"让 agent 自己跑、同时管多个会话"的方式。

```
/goal <条件>                  设定完成条件。智能体跨多个回合自动工作，
                              不再每步问你，同时跟踪已用时间、轮次、
                              token 成本，直到条件达成。例子：
                                /goal "全部预分析诊断通过且 pre-mortem
                                       返回 LOW-RISK"
                              适用：边界清晰、不需要人介入中间步的多步任务。

/workflows                    v2.1.154+（Opus 4.8）：Dynamic Workflows
                              研究预览。让 Claude 设计一套多步工作流，
                              它会写出编排脚本，在后台同时调度数十到
                              上百个子智能体，共享一份可恢复状态。
                              `/workflows` 打开仪表盘，列出所有运行
                              （排队 / 运行中 / 完成 / 失败），可以挑
                              一个 peek 看进度。社会科学的典型用法：
                              一篇论文一个 workflow，每一步是一个
                              scholar-* 技能，scholar-respond 的审稿团
                              是 fan-out 节点，scholar-verify 是
                              fan-in 节点。仅 Max / Team / Enterprise
                              方案和 API 可用。

/bg   (别名: /background)     把当前会话切换到后台 agent 模式。终端
                              回到 shell 提示符；agent 在你机器上继续
                              无头运行。稍后从 `agent view` 重新接管，
                              或用 `/resume <session-name>` 直接接回。
                              从 shell 起的 `claude --bg` 后台会话现在
                              也会出现在 `/resume` 列表里，标记为 `bg`。

/effort                       速度 vs. 推理深度的滑块。Opus 4.8 你常用的几档：
                                  low | high（默认）| xhigh | max
                              （还有其他档位；跑 /effort 看完整列表）
                              `xhigh` 适合识别策略备忘、理论稿、对抗性
                              审稿；`max` 留给"最难的那一次 verify
                              复跑、不计 token 也要把它对上"的场合。
                              日常编辑回到 `high`（或 `low`）——
                              `xhigh` / `max` 又慢又贵。

/focus                        在普通紧凑视图与详细 transcript 视图之间
                              切换。详细视图会展示每个工具的输入 / 输出，
                              是 /scholar-verify 和 scholar-code-review
                              跑的时候应该开的。

/code-review [--fix]          v2.1.152+：审当前 diff。`--fix` 会在审完
                              之后直接把建议的修改写到工作树里，把
                              复用、化简、效率改进直接做成"待提交"。
                              要 6-agent 大盘子用 `scholar-code-review`；
                              提交前的轻量 pass 用 `/code-review --fix`。

/simplify                     v2.1.154+：只做清理的审查，自动把
                              重复代码 DRY 掉、死分支砍掉、命名收紧。
                              建议在 `scholar-replication` 打包前跑一遍，
                              避免把第一版脚手架带进发布包。
```

要同时管多个后台会话，先从任何一个 Claude 会话退出（`/exit` 或关掉标签页），然后在 shell 里跑：

```bash
$ claude agents       # 如果你装的 Claude Code 版本带这个命令
```

这就是 **Agent View** —— 一个单屏仪表盘，列出你机器上所有 Claude Code 后台会话，按状态分组：`Needs Input` / `Working` / `Completed`。在里面你可以新建会话、不接管就 peek 看输出、接管会话继续追问、重命名、关闭。每个后台会话都是一个完整的 Claude Code 对话，由 supervisor 进程托管，跨终端重启都不丢；关 iTerm 不会让 agent 停。macOS 上的后台 agent 现在还能跨 Claude Code 升级活下来（v2.1.153+）。若你装的版本识别不出 `claude agents`，就退回到每个会话各开一个终端标签页。

从 shell 起一个新的后台会话时，可以直接预配置好它需要的一切，不用接管进去再改：

```bash
$ claude agents \
    --add-dir ../shared-cache \
    --settings ./.claude/settings.bg.json \
    --mcp-config ./.claude/mcp.json \
    --plugin-dir ~/.claude/plugins/open-scholar-skill \
    --permission-mode acceptEdits \
    --model claude-opus-4-8 \
    --effort xhigh \
    --dangerously-skip-permissions   # 只在 worktree 里用
```

多数工作坊参与者不会用到完整的 flag 集——但 `--model` + `--effort` 让你能在前台用 `claude-sonnet-4-6` 做日常编辑的同时，在后台开一个"高 effort 的 Opus 4.8 + xhigh"会话专门跑理论那一段。

工作坊用例：

- 用 `/goal` 跑无人值守的技能链（`scholar-eda → scholar-analyze → scholar-code-review`）。
- 用 `/workflows` 做端到端论文编排：一个分派出去的 workflow 把 `scholar-init → scholar-lit-review-hypothesis → scholar-design → scholar-eda → scholar-analyze → scholar-verify` 全部跑完，你正好回邮件。
- 用 `/bg` + `agent view` 同时跑两篇论文（一篇 CFPS、一篇 CGSS），不必同时盯两个终端。
- 仅在写理论 / 识别 memo 时用 `/effort xhigh`；当 scholar-verify 反复纠同一处数字对不上、需要最深一档复查时才上 `max`；写 Results 之前调回 `high`。
- 任何分析脚本改动之后跑 `/code-review --fix`；打包 replication 之前跑 `/simplify`。
- 任何 `scholar-verify` 跑之前开 `/focus`（详细视图），方便看每个验证 agent 实际读了什么。

#### 权限模式

Claude Code 有**六种**权限模式，都通过同一个 `Shift+Tab` 循环或 `--permission-mode <name>` CLI flag 切换。下方模式名是 Claude Code 内部使用的精确标识符。

| 模式 | 行为 | 适用 |
|---|---|---|
| **`default`** | 每个工具 / 路径首次使用时弹出确认 | 学习阶段、敏感数据、首次跑某项目 |
| **`acceptEdits`** | 自动通过文件编辑和常见文件系统命令；其他工具仍提示 | 在本目录里你已经信任智能体做常规编辑 |
| **`plan`** | 只读“探查”模式——智能体必须先写计划，未获批准前不能编辑、不能跑命令 | 任何破坏性或昂贵的多步操作之前 |
| **`auto`** | 自动执行一切而不提示，但有独立的安全分类器审查每个动作，拦截越权、外泄数据、生产部署、force-push 等 | 你信任大方向的长程自治任务（需符合条件的账户 + 较新的模型） |
| **`dontAsk`** | 自动拒绝任何本会弹确认的操作——只有匹配 `allow` 规则的工具和只读命令能跑 | 锁定的 CI / 脚本化、非交互运行 |
| **`bypassPermissions`** | 跳过所有权限提示与安全检查（仍有 circuit-breaker 拦住像 `rm -rf /` 这类灾难） | 仅限 sandbox / worktree 实验，见下方安全规则 |

> **关于可用性。** 六种模式都有文档记载，但某个会话里你能用到哪些取决于你的账户和启动方式。`auto` 只有当账户符合条件（所有套餐、较新的模型如 Opus 4.6+/Sonnet 4.6，且在 Team/Enterprise 上管理员已开启）时才出现在 `Shift+Tab` 循环里；`dontAsk` 从不出现在循环里，只能用 `--permission-mode dontAsk` 设定。做工作坊演示前先用 `/help` 确认你装的版本暴露了哪些。

```
Shift+Tab            循环切换 default → acceptEdits → plan，再循环回来。
                     auto 仅在账户符合条件时进入循环；bypassPermissions
                     需以启用 flag 启动后才加入；dontAsk 从不出现在循环里。
                     当前模式名显示在状态栏。

/permissions         打开交互权限 UI，查看 / 编辑各模式所读取的
                     allow / ask / deny 规则。
```

也可以启动时直接进入某模式：

```bash
$ claude --permission-mode plan        # 进入 plan mode 启动
$ claude --permission-mode auto        # 进入 auto mode 启动
$ claude --dangerously-skip-permissions
# 等价于 --permission-mode bypassPermissions
```

#### Auto mode 与 bypass mode —— 高级模式，请先读完再用

`auto` 与 `bypassPermissions` 改变了“是否需要你确认”的契约。开启之前先看清安全规则。

- **`auto`** —— 智能体可以自主执行一串低风险任务，但遇到破坏性 / 影响共享状态的操作仍会停下问你（`git push`、`rm`、PR 评论、跨项目网络调用）。本项目内的文件编辑、工具调用自动通过。
- **`bypassPermissions`**（即 `--dangerously-skip-permissions` CLI flag）—— **每一个工具调用**都自动通过，包括破坏性的：`rm -rf`（在 circuit-breaker 限度内）、`git reset --hard`、`git push` …… 都不再问你。

**安全规则——开启前必读。**

1. **绝不要在你输不起的项目里用 `bypassPermissions`。** 它适合 sandbox repo、临时 worktree、CI 容器，**不**适合你的博士论文目录。
2. **`bypassPermissions` 要在 `git worktree` 里跑，不要在主 checkout 上跑。** 安全模板：
   ```bash
   $ git worktree add ../sandbox-experiment -b experiment
   $ cd ../sandbox-experiment
   $ claude --dangerously-skip-permissions
   ```
   智能体把 sandbox 弄坏了，删 worktree 重来；主分支毫发无损。
3. **绝不要在 `scholar-safety` 标了 LOCAL_MODE 的文件上用 `bypassPermissions`。** LOCAL_MODE 的意义就是逐次确认；bypass 把这个机制吃掉了。敏感数据会话只用 `default` 或 `acceptEdits`。
4. **`auto` 是更安全的折中。** 它允许智能体把任务链起来不打断你，但破坏性 / 对外效果操作仍会停下。日常实现工作用 `auto`；首次接触敏感项目不要用。
5. **长跑后必看 `/usage`。** `auto` 与 `bypassPermissions` 是“突然账单”出现的主要场景。

总规则：**给 Claude 的自主性越高，你的项目结构、权限、安全扫描就越重要。** Bypass mode 不是 `scholar-init` 的替代品；它是已有规范的放大器。

### 3.3 CLAUDE.md —— 项目的持久简报

项目 `CLAUDE.md` 有两个写入源，互相合作不冲突：

1. **Claude Code 内置 `/init`** —— 写用户作者的项目简报：自己的约定、禁止动作、目标期刊、项目特定说明。
2. **`/scholar-init` 和 `/scholar-full-paper` Phase 0** 各自写入一个用 `<!-- scholar-full-paper:BEGIN auto-rules vN -->` … `<!-- END auto-rules -->` 包裹的自动管理区块。该区块**幂等**且**非破坏** —— 标记外的用户内容原样保留。

自动管理区块有两种 profile：

- **Lean（`v2-lean`，约 50 行）** —— 由 `/scholar-init` Step 1.2.5 写入。仅承载跨 scholar-* 技能的通用规则：稿件文件禁用破坏性正则、客观性 Mandate、数据安全栈 + LOCAL_MODE 范围、引用规则、跨技能工作流（xelatex、`viz_setting.R`、文件版本控制、验证协议）。
- **Full（`v2-full`，约 230 行）** —— 由 `/scholar-full-paper` Phase 0 写入。lean profile **加上**：Pacing Discipline（10 条规则 + ASK / DO-NOT 列表）、G3 诚实停止模板、G4 决策点记忆表、real-agent dispatch heuristic、各 Phase 契约（Phase 11/5.5/10/10.5）、稿件实质规则（Abstract + Limitations）、dispatch manifest 来源链。

**升级方向单向：**第一次跑 `/scholar-full-paper` 时 lean 自动升级为 full。Full → lean 不允许 —— 一旦编排器规则装上，后续 `/scholar-init` 不会把它们抹掉。这样保证用过完整流水线的项目不会被无意中降级。

顺序无所谓：先 `/init` 再 `/scholar-init` 或反过来，结果一样（一个用户区块 + 一个自动管理区块，用标记隔开）。每次 `scholar-init` 或 `scholar-full-paper` 运行时自动管理区块都刷新一遍，插件规则迭代时你的 `CLAUDE.md` 自动跟上。

这个文件以后每次在该目录下开会话都会被读进上下文。用户作者区块（标记外）适合写：

```markdown
# CLAUDE.md — digital-divide-china-cfps

## 数据
- CFPS 原始 .dta 在 data/raw/，永不手工修改。
- 处理后的面板：data/processed/cfps-panel-long.rds，
  仅由 01-build-sample.R 生成。

## 规范
- R 包统一用 tidyverse + fixest + marginaleffects；不用 data.table。
- 图：ggplot2 + viz_setting.R；PDF + PNG，7×4.5 inch，300 dpi。
- 目标期刊：Social Forces；描述/分解设计。

## 禁止
- 永不把 hukou 称作 "treatment"；这是描述性论文。
- 未经我批准不要 git push。
- 当前会话不读 data/raw/*.dta 原始行。
```

把它当实验室手册。**不要**放密钥、原始私人数据或几百页的长文档。

### 3.4 把内容塞进会话的几种轻量办法

新手最容易忽略的事：Claude Code 有三种比“打字喂给 agent”轻得多的方式，把文件、命令、截图带入对话。每种都只差一个按键。

**`@路径/文件` —— 文件引用。** 输入框里敲 `@`，Claude 弹出路径补全器，Tab 接受。文件像贴进上下文那样被读入，但提示词本身保持短，路径被原样记录。这是把代码本、初稿、CSV 表头塞给 agent 最干净的方式：

```
> 读 @data/raw/cfps-2020-codebook.pdf，列出所有衡量上网行为的变量。
```

`@dir/` 一次附整个目录（agent 收到的是递归列表，不是全部内容）。

**`!command` —— shell 直通。** 提示词以 `!` 开头，整行去到你的 shell 跑，结果回插到对话里。**不会**弹工具权限框 —— 你自己的 shell，你自己负责：

```
> !wc -l data/processed/*.csv
> !git status -s
> !Rscript scripts/01-build-sample.R
```

想顺手扔个 `ls`、`git diff`、`head -n 5 file.csv` 进对话，这是最快的路 —— 不必让 agent 提议一次 Bash 调用。

**拖放（与粘贴）。** 把文件从访达 / 文件管理器拖到 Claude Code 终端窗口，绝对路径会落到光标处。一次性附件（审稿意见的截图、刚下的 PDF）特别合适。macOS 上 `Cmd+V` 直接粘图，Claude Code 会把图写到临时路径再引用。

**自检：** 试一下 `@CLAUDE.md` —— Claude 应该悄悄读完，而**不**弹出 Read 工具调用提示。如果看到了，那是因为你敲的是 `>` 而不是 `@`。

### 3.5 选对模型 —— 也选对工具

`/model` 在会话内打开模型切换器，**不必重启会话**。默认 `/model` 只对当前会话生效——按 `d` 把它设成未来会话的默认（v2.1.144+）。取舍很直接：一轴是速度与成本，另一轴是推理深度。

| 模型 | Model ID | 用途 | 大致定位 |
| ---- | -------- | ---- | -------- |
| **Claude Haiku 4.5** | `claude-haiku-4-5` | EDA 摘要、小重构、轮询任务、常规文件编辑、安装日志 | 最快、最省 |
| **Claude Sonnet 4.6** | `claude-sonnet-4-6` | 多数 scholar-skill 运行：分析、写作、citation、验证 | 平衡 |
| **Claude Opus 4.7** | `claude-opus-4-7` | 稳定的高质量旗舰；现在是 Fast 模式的默认模型 | 慢、贵 |
| **Claude Opus 4.8** | `claude-opus-4-8` | 主力旗舰（2026-05-28 发布）。理论、识别 memo、对抗性审稿、最难的验证；配 `/effort xhigh` 或 `/effort max` | 慢、很贵 |
| **Claude Fable 5** | `claude-fable-5` | 新的顶配模型（2026-06-09 发布）。能力天花板——前沿推理、重视觉任务（从密集的科学图表里读出精确数字）、以及 Opus 4.8 配 `/effort max` 仍不够时的验证 | 最慢、约 2× Opus 4.8 |

**4.8 改了什么。** Opus 4.8 把 SWE-bench Verified 拉到 88.6%（4.7 是 87.6%）、SWE-bench Pro 拉到 69.2%（4.7 是 64.3%）；USAMO 2026 数学从 69.3% 跳到 96.7%；1M-token 长上下文检索几乎翻倍（GraphWalks 1M：68.1% vs. 40.3%）。对"氛围式研究"最关键的变化是*代码诚实度*：Anthropic 报告 Opus 4.8"大约比 Opus 4.7 少四倍地让自己写的代码瑕疵静默通过"——意味着 scholar-analyze 与 scholar-compute 的输出里更少出现你看不见的回归。注意点：提示词注入的稳健性略有回退（Opus 4.8 攻击成功率 9.6%，4.7 是 6.0%），所以数据敏感项目不要因此放松 safety-status 关卡。

**Fable 5 —— 新的天花板。** 2026-06-09，Anthropic 发布了 **Claude Fable 5**（`claude-fable-5`），这是其最强（Mythos 级）模型家族里第一个公开可用的成员，也是你现在能调用的最强模型。它在几乎所有测过的基准上都是 state-of-the-art——软件工程（在 Cognition 的 FrontierCode 上即便用 medium effort 也居首）、知识工作（Hebbia Finance Benchmark 最高分）、科研，尤其是*视觉*：它能从密集的科学图表里读出精确数字，还能从截图重建一个 Web app 的源码。定价为**每百万 input / output token $10 / $50**——大约是 Opus 4.8 的两倍，也是 Anthropic 通用可用模型里最贵的。内置防护会把高风险提示（网络安全、生物/化学、模型蒸馏）改由 Opus 4.8 回答，触发率不到 5% 的会话。可用性：**2026 年 6 月 9–22 日**在 Pro、Max、Team、按席位计费的 Enterprise 套餐上免费包含；6 月 23 日后改走 credits，直到容量允许时才完全恢复到套餐内。（其无防护的同胞 **Mythos 5** 是同一底座、放开了部分防护，仅限受信任访问——工作坊项目用不上。）做"氛围式研究"时，只在 Opus 4.8 配 `/effort max` 仍不够、或任务确实重视觉时才动用 Fable 5；Opus 4.8 仍是日常旗舰，而 Fable 在 6 月 23 日后按 credits 计费，一直挂着很容易超支。

**Fast 模式**（Claude Code 的 `--fast` flag 与 `/fast` 开关）现在默认用 Opus 4.7（v2.1.138 之前默认是 Opus 4.6）。配 Opus 4.8 的 Fast 模式以 2× 标准价拿 2.5× 速度——每 token-秒大约比之前 Opus 4.7 的 Fast 模式便宜三倍。Fast 模式适合大批量的 scholar-monitor 抓取、scholar-eda 重跑、以及任何"agent 要跟得上你打字"的场合。

常见的成本失误：整条 CFPS 流水线一直挂着 Opus。`scholar-monitor`、安装步骤、大规模机械编辑切到 Haiku；多数分析与写作切到 Sonnet 4.6；理论部分、识别 memo、pre-mortem、最终对抗性审稿才切到 Opus 4.8 配 `/effort xhigh`。第一次端到端跑完后用 `/usage`（v2.1.149+ 的"按 skills / subagents / plugins / MCP 拆账"视图）确认最大的成本项在哪，再决定要不要给那一步上 `/effort max`。

最常见的成本错误是整条 CFPS 流水线都开 Opus。`scholar-monitor`、安装步骤、大块机械改写换成 Haiku；只有理论段、识别 memo、pre-mortem、最终对抗性审稿才上 Opus。

**`/agents` —— 管理与启动子智能体。** 子智能体（subagent）**不**等于 skill。

- **Skill**（所有 `scholar-*`）是命名工作流：一份 SKILL.md 加上 assets/references；通过 `/skill-name args` 调用。
- **Subagent** 是带**独立上下文窗口**的轻量工作者，有自己的工具和提示词，返回单个答案。Skill **内部**会调 subagent（例如 `scholar-code-review` 并发起六个 reviewer subagent）。

工作坊里你大概率不会自己写 subagent。但如果想跨项目复用比如一个"citation-fact-checker" subagent，`/agents` 就是列出、编辑、新建它的命令。

**WebFetch 与 WebSearch —— 你最先碰到的两个 web 工具。** Claude Code 既能抓取已知 URL，也能跑搜索 —— 这正是 `scholar-lit-review`、`scholar-monitor`、`scholar-citation` 背后用的工具。

- **`WebFetch(url)`** —— 下载单页面，把渲染后的文本喂给 Claude。每个新域名首次使用时弹权限框。
- **`WebSearch(query)`** —— 跑搜索返回结果列表。首次弹框；结果**链接**可被 WebFetch 接力。

权限含义：处理敏感数据的项目，往往应该**把 WebFetch 限制在学术域名白名单内**（`crossref.org`、`openalex.org`、`*.gov` 等），防止 agent 把含参与者文本的 query 发到陌生站点。配置位置：`/permissions` 或 `.claude/settings.json`。

### 3.6 MCP —— 接入外部数据源

**Model Context Protocol（MCP）** 是 Claude Code 跟外部系统对话用的开放协议，省去你写自定义插件的工夫。一个 *MCP server* 暴露 tools（Claude 可调用的函数）与 resources（Claude 可读的文件），走小型 JSON 协议；Claude Code 是 *client*。装一次 server，它的工具从此和内置工具并列。

每个 MCP server 都通过三种**原语（primitives）**之一暴露内容；某样东西属于哪个原语，决定了**由谁来触发**它：

| 原语 | 由谁控制 | 是什么 | CFPS 风格示例 |
| ---- | -------- | ------ | -------------- |
| **Tools** | 模型 | Claude 可调用的函数（受你的权限设定约束） | `zotero.search(query)`, `github.create_pr(...)` |
| **Resources** | 应用 | 只读数据，通过静态或模板化 URI 暴露 | `zotero://library/items/<id>`, `github://repos/<org>/<repo>/issues` |
| **Prompts** | 用户 | 预先写好的指令模板，**你**从提示词选择器手动调用 | `/zotero-cite this paragraph` |

这就是为什么有些 MCP 行为在你已授权的权限下自动流转（model-controlled tools），另一些则要等显式的用户触发（user-controlled prompts）。原语的名字告诉你**谁来决定** —— 模型、应用，还是用户。

社会科学研究者最先回本的两个 MCP server：

- **Zotero MCP** —— 把你的 Zotero 库暴露给 Claude。agent 能搜你的 collection、拉论文 PDF + 元数据、自动写进对应 collection。`scholar-lit-review` 之所以能“读完整本地论文”而不是凭空捏造引文，靠的就是它。
- **GitHub MCP** —— 把你的仓库、issue、PR 暴露给 Claude。`scholar-replication`（“根据最近 12 个 commit 写发行说明”，“用这组改动开个 PR”）特别用得上，也是管 `output/` 仓库的好帮手。

其他值得一装：处理本地数据库的 **Postgres / SQLite MCP**；想让 Claude 受控访问项目根目录**之外**的目录（例如 `~/data/` 共享缓存）的 **Filesystem MCP**。

**添加一个 server。** 最简单的路径：

```bash
# Zotero：本地 stdio server（zotero-mcp 这个 Python 包，用 uvx 跑）
$ claude mcp add zotero -- uvx zotero-mcp

# GitHub：官方远程 server。旧的 npm 包 server-github 已弃用；
# 改用托管 endpoint，把细粒度 PAT 放到 header 里。
$ claude mcp add --transport http github https://api.githubcopilot.com/mcp/ \
    --header "Authorization: Bearer $GITHUB_PAT"

$ claude mcp list
```

先从 CLI 查看某个 server 的配置与连接状态，再进会话里看它真正暴露了哪些工具：

```bash
$ claude mcp get zotero      # 查看单个 server 的配置与连接状态
```

```
> /mcp                       # 在 Claude Code 会话里：列出每个已连接 server，
                             # 带工具数量与登录状态
```

（没有 `claude mcp tools` 这个子命令；要看每个 server 的工具清单，用 `/mcp`。）

大多数 server 要凭证（Zotero API key、GitHub PAT）。按 §2.5.3 的做法存进 `~/.api-keys`，从 server 配置里引用；**永远不要**硬编码到 `settings.json`。

**工作坊纪律：** 只在替代方案是“agent 反复编造引文 / PR 描述 / 数据行”时才加 MCP server。MCP 不是免费升级 —— 每多一个 server 就多一处可能把数据送到你没打算去的地方的表面。

### 3.7 在编辑器里跑 Claude Code

多数学员最终是在编辑器里、而不是裸终端里用 Claude Code。三种集成最要紧：

- **VS Code 扩展**（发布者 Anthropic）。从 Marketplace 装；它会加一个 Claude 面板，把编辑器的当前选区、Problems 面板、git diff 绑到对话里。在 WSL2 / SSH-remote / devcontainer 窗口里，它会跟着 remote root 走。
- **Cursor 与 JetBrains 系列。** Cursor 是 VS Code 的分支，装的是*同一个*扩展，行为一致。JetBrains 系列用的是 JetBrains Marketplace 上*另一个独立*的 Claude Code 插件；它在 IDE 终端里跑 Claude Code，所以模式循环和 `--permission-mode` 跟 CLI 一样——工作流相同，包不同。
- **JupyterLab。** 目前没有原生 Claude 扩展，但 JupyterLab 的 *terminal* 标签页和普通 shell 一样 —— 在里面跑 `claude` 即可。RStudio 同理：打开 **Terminal** 面板，运行 `claude`；项目根目录自动是 RStudio 的工程目录。

IDE 接入的会话里会变的：

1. agent 拿得到 IDE 的**当前选区**与**打开文件**作为隐式上下文 —— 你可以说“这个函数”而不必贴代码。
2. 诊断信息（linter、类型错误）自动流入对话，“修一下下面这些类型错”这种提示无须粘贴。
3. diff 视图是 IDE 原生 diff，不是 CLI diff —— 大改动时可读性强多了。

**不**变的：项目根、CLAUDE.md、`.claude/settings.json`、PreToolUse hook、权限模式。IDE 只是前端；agent 与其安全边界跟终端模式完全一致。

### 3.8 Headless 模式、定时任务、团队配置

下面这三件事，是你信任 Claude Code 到愿意让它脱离手动监督之后才用得上。

**Headless / 非交互模式。** 从 shell 脚本或 cron 跑一条提示词：

```bash
$ claude -p "用一段话总结今天 scripts/ 下的提交；保存到 logs/daily-$(date +%F).md"
```

加 `--output-format json` 拿机器可读输出再管道给下游工具。`-p` 模式里**没有**交互批准循环，所以提示词需要的每一个工具都必须事先在项目的 `.claude/settings.json` 里允许。**敏感数据上不要在没白名单的情况下开 headless。**

**GitHub Actions。** Anthropic 官方发布了 `claude-code-action`，可以在每个 PR 上跑 `claude -p`。最简工作流：

```yaml
# .github/workflows/claude-review.yml
name: Claude review on PR
on: [pull_request]
jobs:
  claude:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: "审查 diff 是否出现不当因果语言。"
```

研究中的用法**不**是发功能 —— 是把 CLAUDE.md 里声明的“禁止主张”清单，在每一次动到稿子的 PR 上自动执行一遍。

**`settings.json` 三层 —— user / project / local。** Claude Code 按下面顺序合并三份配置（后者覆盖前者）：

<div class="hb-table-wrap">
<table>
<thead><tr>
<th><strong>文件</strong></th><th><strong>位置</strong></th><th><strong>是否提交</strong></th><th><strong>用途</strong></th>
</tr>
</thead><tbody>
<tr>
<td><code>~/.claude/</code><br><code>settings.json</code></td><td>家目录</td><td>否</td><td>个人偏好：env vars、默认模型、你的全局 hook</td>
</tr>
<tr>
<td><code>&lt;project&gt;/.claude/</code><br><code>settings.json</code></td><td>仓库根</td><td><strong>是</strong>（提交）</td><td>团队共享规则：权限白名单、PreToolUse hook、团队共用的 MCP server</td>
</tr>
<tr>
<td><code>&lt;project&gt;/.claude/</code><br><code>settings.local.json</code></td><td>仓库根</td><td><strong>否</strong>（gitignore）</td><td>本机覆盖：你的个人 API key、“这个目录里始终允许 Read”等私有决定</td>
</tr>
</tbody></table></div>

这种分层很重要：你**提交**的（project 层）是 IRB / 复制包记录的一部分；你**不提交**的（local 层）只属于你的笔记本。**secrets 进 local 层；团队规则进 project 层。**

**OAuth 与 API key 两种登录路径。**

- **OAuth via Anthropic Console** —— 跑 `claude login` 打开浏览器，以你的 Anthropic 账号认证，Claude Code 保存刷新 token。结算走你的 Claude Pro / Max / Team 订阅。**个人研究者首选。**
- **`console.anthropic.com` 的 API key** —— 粘贴 key，结算走 API console。**适合**机构持有 Anthropic 账号、给你发项目级 key、想能按项目撤销访问的场景。

如果机构要求每项目独立审计轨迹，**优先 API key** —— 可以按项目轮换 / 撤销，Anthropic Console 也能按 key 看用量。

**自检：** 三层 settings 配完之后跑一次 `/doctor`，再跑 `claude mcp list` 看注册了哪些 server。如果 `/doctor` 报三层之间不一致，先解决再进 §4。

## 4. 最小安全项目结构

```
digital-divide-china-cfps/
├── CLAUDE.md                  ← 持久项目简报
├── .claude/
│   └── safety-status.json     ← 哪些文件 CLEARED / LOCAL_MODE / HALTED
├── data/
│   ├── raw/                   ← 原始 CFPS .dta，永不手工修改
│   ├── interim/               ← 可再生的中间文件
│   └── processed/             ← 由脚本生成的处理后数据
├── materials/                 ← 中英文问卷与代码本
├── output/
│   └── digital-divide-china-cfps/
│       ├── design/            ← idea、blueprint、变量字典
│       ├── scripts/           ← 所有 R / Python 脚本
│       ├── tables/            ← 回归表、描述表
│       ├── figures/           ← PDF / PNG 图
│       ├── drafts/            ← 各版手稿
│       ├── verify/            ← 验证报告
│       ├── citations/         ← refs.bib、引用日志
│       ├── replication-package/
│       └── logs/              ← 时间戳日志
├── logs/
│   └── init-report.md
└── README.md
```

要点：

- **`data/raw/` 是圣域**，所有变换都必须由 `output/<slug>/scripts/` 里的脚本完成；如果不能从 `data/raw/` 一键再生 `data/processed/`，项目就坏了。
- **`output/<slug>/` 是工作区**，每个技能写到固定子目录，让你随时能找到 `verify/`、`drafts/`、`tables/`。
- **`logs/` 是证据**。验证发现问题时，第一句话永远是“那次跑的时候到底干了什么？”

如果你目前的项目是桌面一堆 `final_v3_REAL.xlsx`，智能体救不了你；它只会让混乱跑得更快。先做 `scholar-init`。

## 5. 练习 1 —— 把模糊请求改写成智能体任务

**用时：** 5 分钟。继续学习前先做。

**模糊版（不要）：**

> “用 CFPS 数据写点关于中国数字鸿沟的东西。”

**智能体级别（要这样写）：**

```
INPUTS（允许读取）
  - data/raw/cfps2010adult_*.dta 至 cfps2020person_*.dta
  - materials/ 下的代码本
  - design/variable-dictionary.csv
TASK（任务）
  - 构建个人–波次面板，限制 16+ 岁；harmonize：
    互联网接入、每周使用小时、户口、教育、世代、性别、家庭规模、省份。
OUTPUTS（产出）
  - data/processed/cfps-panel-long.rds
  - logs/01-build-sample-<timestamp>.log
  - 仅打印一份摘要：按 wave × hukou 的行数。
QUALITY STANDARD（标准）
  - 所有样本限制写在脚本头部。
  - CFPS 缺失代码（-1, -2, -8, -9, -10）一律转 NA。
  - 一条命令可端到端运行：`Rscript 01-build-sample.R`。
AUDIT（审计）
  - 打印每个被读文件的路径，给输出 rds 计算 SHA256。
STOP RULE（停止规则）
  - 任意一波缺超过 3 个预期变量则停下并报告，不要插补。
  - 处理后面板少于 150,000 行则停下。
```

第一版让智能体写论文；第二版让智能体执行一个**可测、有边界、可检查、能停下**的任务。

六个组成部分：

| 元素 | 回答的问题 |
|---|---|
| **Inputs** | 智能体能读什么？ |
| **Task** | 操作是什么？ |
| **Outputs** | 完成时哪些文件必须存在？ |
| **Quality** | 怎样算够好？ |
| **Audit** | 日志里要记录什么？ |
| **Stop** | 满足什么条件必须暂停问我？ |

提示词里最重要的一句话：**“如果无法验证，就明确标记。”** 这一行能改变智能体行为——它允许“不完整”，而不是装作“很有信心”。

## 5A. Claude Code 2026 新特性：动态工作流、子智能体与自动化

**目标：** 搞清楚 Claude Code 近一年新增的能力里，哪些真正改变了你做研究的方式、哪些只是顺手——这样你才能挑对工具，而不是把所有事都硬塞进一个聊天窗口里去硬抗。

第一部分一直把 Claude Code 当成“一个会话里的一个助手”。这个心智模型现在依然成立，但它把 2026 年的大半套能力都晾在了一边。过去一年的版本更新，给智能体加上了**把任务铺开、放到后台跑、按时间表重复、并自动执行你设定规则**的能力。用得好，它能把“写一篇论文的流程”升级成“一个小型研究流水线”；用得糙，它只会让“未经验证的结论”多出更多藏身之处。本手册反复强调的纪律——*任务有边界、产物可检查、标准由人把关*——在自主性升高时只会**更**重要，而不是更不重要。

> 下面这些特性变化很快。请把具体的命令名和默认值当成 2026 年年中的一张快照；当某个东西行为不一样时，在会话里敲 `/help`、并查阅更新日志（`claude changelog` 或官方文档）。*概念*是稳定的，*写法*会漂移。

先给一张速查表，告诉你什么时候该用什么：

| 能力 | 一句话用途 | 在研究里什么时候值回票价 |
|---|---|---|
| **计划模式（Plan mode）** | 动任何文件之前先看计划 | 有风险的重构、任何会改很多文件的操作 |
| **子智能体（Subagents）** | 把一个有边界的活儿交给全新上下文 | 多评审交叉检查、文献初筛、隔离噪音 |
| **动态工作流（Dynamic workflows）** | 在后台铺开、协调一大批子智能体 | 全仓审计、批量重编码、交叉核验式综述 |
| **自定步调循环 / 目标** | 迭代到满足某个条件为止 | “跑到所有测试通过 / 表格能复现为止” |
| **后台任务** | 长任务不卡住终端 | 整条流水线、大批量模型调用 |
| **定时任务**（`/schedule`） | 按时钟跑的例行活儿 | 每日新论文摘要、每周数据质量巡检 |
| **钩子（Hooks）** | 在智能体事件上触发 shell 命令 | 强制执行数据边界、拦截破坏性命令 |
| **技能与插件（Skills & plugins）** | 把一套流程打包一次、到处复用 | `scholar-*` 套件本身*就是*一个技能包 |
| **工作树（Worktrees）** | 互相隔离的并行检出 | 同时跑两种分析而不打架 |

### 计划模式 —— 动文件之前先看计划

按 `Shift+Tab` 在多个权限模式之间切换，其中之一就是**计划模式**。在这个模式下，智能体可以读取、搜索、推理，但在你批准之前**不能改文件、不能跑 shell 命令**。它会产出一份书面计划然后停下来等你。

```
> Shift+Tab  （切到提示栏显示 “plan mode” 为止）
> 读一下建样本脚本和变量字典，然后给我一份方案：加一个省级固定效应的稳健性
  检验。先别写任何东西。
```

对研究者来说，这是最便宜的一份保险：你在自己的分析改动一行之前，就读到了它打算怎么做——改哪些文件、用什么估计量、产出什么。批准它，智能体就切到执行；否决它，则一个字都没动过。

### 子智能体 —— 把一个有边界的活儿交给全新上下文

**子智能体**是主会话委派出去的一个独立 Claude 实例。它在**自己的上下文窗口**里运行，有自己的系统提示词、可选的受限工具清单，甚至可以用不同的模型。主对话拿回来的只是这个子智能体的**总结**——而不是它为了得出结论读过的那 30 个文件。

你其实早就在依赖它了：`scholar-code-review`（“六位评审、一份报告”，第 13 节）和 `scholar-verify` 系列（第 15 节、附录 F–J）就是靠并行派发专职子智能体来工作的。你也可以自定义。往 `.claude/agents/` 里放一个文件：

```markdown
---
name: lit-triage
description: 针对给定的研究问题给论文做相关性初筛，返回一句话判定加引文。
  用于批量文献初筛。
model: haiku
tools: Read, WebSearch, WebFetch
---
你一次只筛一篇论文，对照研究问题判断。
返回：RELEVANT / MAYBE / NOT、一段话理由、以及引文。
绝不编造发现；如果拿不到论文，就直说。
```

然后用大白话提需求（“把这 20 条摘要按数字鸿沟这个问题做初筛”），Claude 就会把每一条路由给 `lit-triage` 这个工作体。把快、重复的活儿派给 `haiku` 还能省钱。第 1 节的规矩依然成立：子智能体的总结描述的是它*打算*做什么——抽查产物，别盲信总结。

### 动态工作流 —— 铺开、协调、并放到后台

这是最受关注的新增能力，也是工作坊被问得最多的一个。**动态工作流**是智能体替你规划并运行一**支**子智能体队伍：Claude 根据你的任务描述写出一段简短的编排脚本，再由运行时执行它——派出许多工作体（任务的独立单元）、同时只跑限定数量的几个、并把中间结果存在脚本变量里，而不是一股脑全塞进你的对话。它跑的时候，你的会话仍然能用。

如果说单个子智能体是“做这一件有边界的活儿”，那动态工作流就是“把这件事*跨数百个单元*做完，再把汇总结果端给我”：

```
> 用一个工作流：对 analysis/ 下的每个 .R 脚本，检查在拟合任何模型之前，是否
  已把缺失值代码（-1,-2,-8,-9,-10）转成 NA。返回一张表：脚本、行号、状态。
  并行跑、再汇总。
```

适合这种模式的研究场景：

- **全仓 / 全语料审计** —— 每个脚本、每个变量、每条图注，用同一把尺子查一遍。
- **批量转换** —— 把 500 个文件拆成独立单元做重编码或重新协调。
- **交叉核验式综述** —— 让几个工作体从*相互独立*的角度调查*同一个*论断，再做对账，而不是只信一次结果。

> **成本与告诫。** 工作流会把 token 开销乘以它派出的工作体数量。*务必先在一小片上试*——一个目录、一个波次、一个问题——确认输出形态对了，再铺开。而且因为运行途中没有人把关，第 5 节的“停止规则”纪律不是可选项：把“如果无法验证，就明确标记”直接写进任务里。

### 自定步调循环与目标驱动

两种让智能体“干到完为止”而不用你盯着的办法：

- **`/loop`** 重复一条提示词。给它一个间隔（`/loop 5m 检查任务跑完没有`）用来轮询，或者让它**自定步调**（`/loop 一直修失败的测试，按需迭代`）由智能体自己决定何时进入下一轮。
- **完成目标**让智能体跨多轮自动连续推进，直到一个可度量的条件达成——“直到 `Rscript 11-analyze.R` 干净跑通、且头条表格与附录 G 对得上”。

它们在分析的“机械尾巴”上最好用：复现一张表、把脚本一条命令跑通、把 linter 清到零。但它们不擅长模糊目标（“把论文写得更好”）——那种永远不会干净收敛，所以把条件设成可二元判定、可核对的。

### 后台任务与监控

长任务——整条流水线、一大批模型调用、慢编译——可以在同一个会话里丢到**后台**跑，你继续干别的。智能体把活儿交出去，跑完通知你，你也可以查看中间输出，而不必盯着一个卡死的终端。对研究来说，这意味着那个 40 分钟的数据构建，和你现在正在做的稿件修订，不再互相挡道。

### 定时任务 —— `/schedule`

`/schedule` 创建按时钟运行的周期性任务（在云端 / 远程配置下，关掉终端也能持续）。你用大白话描述节奏和活儿：

```
> /schedule  每个工作日早 8 点，搜索关于 “digital inequality” 的 arXiv 新论文，
  把每篇的一句话摘要追加到 lit/inbox.md
```

自然的研究用法：早晨的新论文摘要、周五晚上的数据质量巡检、每月一次的日志归档。它会计入你的用量、并以你授予的文件权限运行，所以像对待任何智能体任务一样去框定它的范围。

### 钩子 —— 把数据边界从“指望”变成“强制”

第 1 节说过：智能体的读取边界*就是*你的数据边界。**钩子（Hooks）**让你用机械的方式来强制执行它。钩子是 Claude 在某个事件上自动运行的 shell 命令——工具调用之前（`PreToolUse`）、之后（`PostToolUse`）、会话开始时，等等——而一个 `PreToolUse` 钩子可以**拦截**某个动作。在 `.claude/settings.json` 里配置：

```json
{
  "hooks": {
    "PreToolUse": [
      { "matcher": "Bash",
        "hooks": [{ "type": "command", "command": ".claude/hooks/guard.sh" }] }
    ]
  }
}
```

脚本检查待执行的命令，以非零退出（或返回拒绝决定）来回绝它——比如回绝任何 `rm -rf`，或任何写到 `data/processed/` 之外的操作。这就是你把“请别动原始数据”从 `CLAUDE.md` 里一句礼貌请求，变成一项保证的办法。

### 技能与插件 —— 把一套流程打包一次

**技能（Skill）**是 `.claude/skills/<名字>/` 下的一个文件夹，里面的 `SKILL.md` 装着一套流程；它的全文只有在技能被调用时（`/<名字>`）才加载，所以不用时不占上下文。**`open-scholar-skill` 正是如此**——它是一包技能（`scholar-init`、`scholar-design`、`scholar-verify`……）。**插件（Plugins）**则把技能、子智能体、钩子、MCP 服务器打包到一起，让一个实验室一次安装就能共享整套工具。给学员的启示是：当你发现自己在不同项目里反复敲同一套多步指令时，那就是一个等着被写出来的技能。

### MCP 服务器 —— 接入 Zotero、数据库与网络

**模型上下文协议（MCP）**让智能体把外部工具和数据源当成一等公民的工具来调用。用 `claude mcp add …` 添加（或在 `.mcp.json` 里声明），然后 `/mcp` 查看状态并处理登录。

```
$ claude mcp add --transport stdio zotero -- uvx zotero-mcp
```

对研究来说，这是通往你的文献管理器、结果数据库、笔记服务或可信网络检索工具的桥梁——让智能体直接拉取结构化数据，而不必你手动复制粘贴（从而引入正是第 15 节存在意义所在的那类转录错误）。

### 工作树 —— 不打架的并行实验

**工作树（worktree）**是位于自己分支上的一个独立工作目录。Claude Code 可以在其中跑一个会话——或隔离一个子智能体——这样两条工作线就永远不会覆盖彼此的文件。用 `claude --worktree try-province-fe` 开一个；智能体在那里开发，只有当这个实验值回票价时你才合并它的分支。非常适合“把分析跑两种做法再对比”，而不污染你的主检出。

### 模型、思考强度与快速模式

三个值得知道的旋钮：`/model` 在 Opus（推理最深）、Sonnet（均衡）、Haiku（又快又省——适合子智能体和初筛）之间切换；**思考强度（effort）**设置用思考深度换速度和成本；**`/fast`**（在较新的 Opus 4.x 上）让日常活儿的回答明显更快。一个合理的默认：设计、分析、验证用 Opus，批量机械的子智能体活儿用 Haiku。此外还有 **`/ultrareview`**——一个由你手动触发、计费的多智能体评审，针对你当前分支或某个 PR，比 `scholar-code-review` 更重、更独立的第二意见。

### 关于自主性与验证的一点提醒

本节里的每一项能力，都把工作从那个“被盯着的单一会话”里**挪了出去**，挪向队伍、时间表和后台运行。这是实打实的效率提升，也是实打实的风险集中：智能体无人值守地做得越多，一个错数字在被人看到之前就能跑得越远。所以工作坊的核心一课（第 15 节）会随着这些工具一起放大——你授予的自主性越多，验证与可检查产物就越是不可妥协。新能力，同一份契约：**问题和标准由你把关，执行由智能体负责。**

**有一样产物让这一切可检查。** 现在每次 `/scholar-*` 运行都会留下一条 **推理–行动–观察（RAO）轨迹**——一个只追加的 `logs/trace-<skill>-<date>.ndjson`，每一步一条 `{reasoning, action, observation, refs, status}` 记录。你看的 `process-log-*.md` 是它的*渲染视图*；覆盖检查会让任何没留下轨迹的 phase 直接 RED 失败。被派出的子 agent（评审、验证）会写一个 `.trace.ndjson` 边车，由编排器汇入。隐私规则：轨迹只记结论、计数和文件引用——**绝不记原始行、引文或 PII**，LOCAL_MODE 下只记派生的聚合量。

# 第二部分：Open Scholar Skills 全流程

这是工作坊的核心。我们用 Open Scholar Skills 一步步搭一篇 Social Forces 风格的中国数字鸿沟论文。下面每一段代码都来自 2026 年 5 月 4–5 日真实运行的项目。Slug：`digital-divide-china-cfps`。

## 6. `scholar-init` + `scholar-safety` —— 从安全开始

**目标：** 创建标准项目结构、对每个文件分类、写下后续技能要遵守的安全契约。

### 6.1 跑 `scholar-init`

```
> /scholar-init --slug digital-divide-china-cfps \
                --data ~/data/cfps/raw \
                --materials ~/data/cfps/materials
```

它会：

1. 建好 §4 中的目录树。
2. 把原始 `.dta` 软链接（或拷贝）进 `data/raw/`。
3. 把代码本进 `materials/`。
4. 用 `file`、`wc`、`grep`、`awk` 在**本地**对每个文件做安全扫描——Claude 只看到统计与模式类别，**看不到原始值**。
5. 写出 `logs/init-report.md` 与 `.claude/safety-status.json`。

真实运行的截选：

```
[scholar-init] Creating project: digital-divide-china-cfps
[scholar-init] Ingesting 38 raw files from data/raw ... ok
[scholar-init] Ingesting 19 materials files ... ok
[scholar-init] Running safety scan ...
  cfps2010adult_201906.dta            : CLEARED        (de-identified PIDs)
  cfps2018crossyearid_202104.dta      : CLEARED        (cross-year ID file)
  cfps2020person_202306.dta           : NEEDS_REVIEW   (location items, COVID)
  CFPS_2020_QnrAdult_EN.pdf           : CLEARED        (codebook)
  ...
[scholar-init] Wrote .claude/safety-status.json
[scholar-init] DONE — 35 CLEARED, 3 NEEDS_REVIEW, 0 HALTED
```

### 6.2 用 `scholar-init review` 解决 NEEDS_REVIEW

**所有 NEEDS_REVIEW 没解决之前，不能进入头脑风暴或分析。**

```
> /scholar-init review
```

每一个 NEEDS_REVIEW 文件都会逐一过一遍：

```
File: cfps2020person_202306.dta
Reasons flagged:
  - Contains community-level codes (ck01, ck02) below-county granularity
  - Contains COVID-related items that may be sensitive
Options:
  [c] CLEARED          - 直接读取
  [l] LOCAL_MODE       - 仅本地脚本读取，原始行不进上下文
  [a] ANONYMIZED       - 替换成派生 / 聚合文件再让 Claude 读
  [o] OVERRIDE         - 直接读取，但需要书面理由进日志
  [h] HALTED           - 本项目禁读
Choice [c/l/a/o/h]:
```

CFPS 的人户文件通常选 **`l` (LOCAL_MODE)**：脚本能跑回归出表出图，**原始行不会进入 Claude 的上下文窗口**。这是真实的隐私边界，不是口号。

### 6.3 检查 `safety-status.json`

```bash
$ jq . .claude/safety-status.json | head -30
```

```json
{
  "_safety_level": "standard",
  "/Users/you/digital-divide-china-cfps/data/raw/cfps2010adult_201906.dta": "LOCAL_MODE",
  "/Users/you/digital-divide-china-cfps/data/raw/cfps2018crossyearid_202104.dta": "CLEARED"
}
```

sidecar 是一个**扁平**映射——绝对文件路径 → 状态字符串——外加唯一的元键 `_safety_level`。（对象型条目、或相对路径键，都算 schema 违规，会让守卫 fail-closed；守卫的查找没有相对路径回退。）

后面**每一个**技能在动手前都先读这份文件。LOCAL_MODE 状态下分析脚本必须只输出汇总，`scholar-analyze` 会拒绝打印原始行。

**自检：** 打开 `logs/init-report.md`，能不能指出某个 LOCAL_MODE 文件并解释为什么？不能就先别 brainstorm。

## 7. `scholar-brainstorm` —— 拓宽问题菜单

**目标：** 产出一份排序过的候选研究问题清单，每个带变量、方法草图、风险。**不要**让它替你决定博士论文；让它**拓宽菜单**。

### 7.0 三种模式 —— 由输入自动判定

`scholar-brainstorm` 有**三种模式**，会根据你给的输入自动选：

| 模式 | 触发条件 | 你拿到什么 |
|---|---|---|
| **MATERIALS** | 代码本、问卷、变量字典（`.pdf` / `.md` / `.txt` / `.docx`），无原始数据 | 理论驱动排序：15–20 个候选 RQ，按 **5 个维度**打分（新颖性、数据可得性、理论、识别、发表潜力）。无经验信号检验。 |
| **DATA** | 原始数据文件（`.csv` / `.dta` / `.rds` / `.sav` / `.xlsx` / `.parquet`） | 理论驱动排序 **+ 经验信号检验**：在你的数据上真实跑双变量效应（Cohen's d、η²、Cramér's V、r），按 **6 个维度**打分（上面 5 项 + 20% 经验信号权重）。 |
| **PAPER** | 已发表论文 PDF、DOI、或粘贴的摘要 | “后续论文”生成器：抽取种子论文的发现 + 局限 + 未来方向，可选地调用 **SciThinker-30B** 做 AI 选题，再扩展成 15–20 个 follow-up RQ，按 5 维度打分。 |

自动判定看文件后缀，对 PDF 还会看内容——"Abstract / Introduction / Methods / References“判定为 PAPER；”Variable / Codebook / Questionnaire"判定为 MATERIALS。

三种模式共享下游流水线：文献扫描 → Top-10 短列表 → 五角色评估面板（五个 Task 调度的评估 prompt —— 理论家、方法学家、领域专家、编辑、devil's advocate —— `scholar-brainstorm` 内部角色，不是 `.claude/agents/` 中的具名 agent）→ 精修 Top-10 → 研究计划概览 → 执行摘要。差异只在 Step 0–4。

CFPS 数字鸿沟例子用的是 **MATERIALS** 模式。下面先讲 MATERIALS，再分别展示同一个项目在 **DATA** 与 **PAPER** 模式下会是什么样。

### 7.1 MATERIALS 模式 —— 从代码本起步

适用：**有代码本/问卷但还没拿到原始数据**——可能是申请待批，或者你刻意先要一份理论驱动菜单再碰数据。

#### 7.1.1 运行

```
> /scholar-brainstorm materials top 5 RQs on digital divide in China,
                       target Social Forces, descriptive/decomposition
```

它检测到 MATERIALS 模式（仅有代码本，没有打开 `data/raw/`），基于问卷与变量字典推理并查证外部来源。一般 4–7 分钟，本次成本约 $1.20。

#### 7.1.2 真实输出（节选）

来自 `output/.../scholar-brainstorm-...top5-summary-2026-05-05.md`：

```markdown
# 研究问题头脑风暴 — 执行摘要
## 中国数字鸿沟（CFPS 材料）
*由 /scholar-brainstorm 于 2026-05-05 生成*
*运行模式：MATERIALS*

## Top 5 RQs

### #1：接入趋同，使用分化
**RQ：** 2010–2020 年中国，户口、教育、世代在互联网接入上的差距是否
缩小，而生产性使用、使用强度、使用广度的差距持续或扩大？
**变量：** U201, U202, U250M, U701-U705, hukou, education, cohort,
gender, income, household composition.
**为什么最强：** 最适合做旗舰论文；利用 CFPS 面板结构区分第一层接入
与第二层生产性使用。
**方法草图：** 面板模型，wave/省控制，可行处加入 individual FE，对农
业户口和世代差距做 Oaxaca 分解。

### #2：疫情期间的远程工作鸿沟  […]
### #3：在线学习产出鸿沟          […]
### #4：老年群体数字健康与社会连接鸿沟  […]
### #5：信息信任、隐私关切与平台依赖    […]

## 推荐
以 RQ1 作为主论文。[...]
```

#### 7.1.3 写入磁盘的文件（MATERIALS 模式）

```
output/<slug>/
├── scholar-brainstorm-<slug>-<date>.md         ← 完整报告（15–20 个候选）
├── scholar-brainstorm-<slug>-summary-<date>.md ← 执行摘要（Top 5 + 推荐）
└── logs/process-log-scholar-brainstorm-<date>.md
```

外加每份的 `.docx`、`.tex` 与 `.pdf`（pandoc 渲染）。

#### 7.1.4 检查

打开完整文件，查四件事：

1. **变量是否真实存在** —— `U201`、`U250M` 在代码本里能找到吗？
2. **外部引用是否可解析** —— 点开链接，看能否打开。
3. **风险是否具体** —— RQ5 正确指出“部分 2020 年题项是受限数据”。
4. **是否有过宽的问题** —— RQ4 “互联网使用是否改善老年人健康”过宽，输出已诚实标出。

**自检：** 选定一个 RQ 往下走。本手册接下来选 **RQ1**：可行、与理论相关、可测量。

### 7.2 DATA 模式 —— 从数据本身起步

适用：**原始数据已经在磁盘上、且 `scholar-init` 已经分类**。DATA 模式比 MATERIALS 模式多两件事：

1. **安全闸门** —— 在读任何文件前，先查 `.claude/safety-status.json`（`scholar-init` 写下的 sidecar）。任意输入文件状态为 `NEEDS_REVIEW:*` 或 `HALTED`，技能**直接拒绝运行**，要求你跑 `/scholar-init review`。如果 sidecar 不存在，则退化为本地 `grep` 扫描，**只**返回 PII / HIPAA / 受限数据标记的**计数**，不返回匹配值本身。
2. **经验信号检验** —— 对 15–20 个候选 RQ，技能写一个 R 脚本（`scripts/brainstorm-signal-tests.R`），先送 3 个智能体做执行前代码审查，然后才跑。每个候选拿到一个真实双变量效应量（连续结果用 Cohen's d，方差分析用 η²，列联表用 Cramér's V，相关用 Pearson's r）和一个信号等级：**STRONG**、**MODERATE**、**WEAK**、**NULL**、**MECHANISM PLAUSIBLE**、**MODERATION DETECTED** 或 **UNTESTABLE**。

Top-10 评分按 6 个维度加权——新颖 20%、数据可得 15%、理论 20%、识别 15%、发表潜力 10%、**经验信号 20%**——而不是 MATERIALS / PAPER 的 5 维度。

#### 7.2.1 运行（如果 CFPS 例子走 DATA 模式会是这样）

```
> /scholar-brainstorm data/raw/cfps_panel_long.rds
                     top 5 RQs on digital divide in China,
                     target Social Forces
```

如果 `scholar-init` 已把这个文件标为 `LOCAL_MODE`，技能会**继承**这个决定（“scholar-init 握手”），所有经验检验都通过 `Rscript brainstorm-signal-tests.R` 跑——Claude 自己**从不**`Read` 数据。

#### 7.2.2 你会看到 —— 信号表

DATA 模式典型的信号表长这样：

```
EMPIRICAL SIGNAL TABLE  (sample sizes from cfps_panel_long.rds)

| RQ | x_var       | y_var       | test   | n     | effect_size      | p       | signal   |
|----|-------------|-------------|--------|-------|------------------|---------|----------|
| 1  | hukou_rural | y2_hours    | t-test | 119k  | d = -0.42 (med.) | 1.4e-5  | STRONG   |
| 1  | cohort      | y1_access   | χ²     | 148k  | V = 0.31 (med.)  | <1e-60  | STRONG   |
| 2  | mobile_only | covid5      | t-test | 34k   | d = +0.18        | 4.2e-3  | MODERATE |
| 4  | u703_social | sf12_mh     | r      | 41k   | r = +0.11        | 7.8e-4  | WEAK     |
| 5  | u11_wechat  | u13_trust   | r      | 26k   | r = +0.08        | 0.04    | WEAK     |
```

技能在表旁打印的提醒（原话）：

- *信号是双变量的——这里没处理混杂。*
- *本阶段**不做**多重检验校正；任何单一 p 都不能当作确证检验。*
- *NULL ≠ “没意思”；可能是被其它变量中介。*

#### 7.2.3 执行前代码审查

任何 `Rscript` 真正跑起来之前，技能并行派出三个评审智能体审查信号检验脚本：

- `review-code-correctness` —— 变量引用、NA 处理、off-by-one
- `review-code-statistics` —— 检验类型与变量类型是否匹配，是否正确使用 `effectsize` 包
- `review-code-data-handling` —— 样本限制、缺失值代码、与代码本对齐

输出汇总到 `scripts/brainstorm-signal-tests-review.md`，带严重等级。执行闸门有四种结局：

- **PROCEED** —— 无 CRIT/MAJOR；运行脚本。
- **FIX-AND-RERUN** —— 修复被指出的问题，重新审查，再跑。
- **OVERRIDE** —— 用户输入 ≥20 字符的理由；进 process log。
- **HALT** —— 停止技能；没有候选值得照原样跑。

也就是说，**DATA 模式在数据被碰之前就留下了完整审计轨迹**——这正是工作坊要教的纪律。

#### 7.2.4 写入磁盘的文件（DATA 模式）

除了 MATERIALS 模式的两份文件，DATA 模式还会写：

```
output/<slug>/scripts/
├── brainstorm-signal-tests.R                  ← 真实 R 脚本（可审计）
├── brainstorm-signal-tests.log                ← 运行 stdout
├── brainstorm-signal-tests-review.md          ← 三智能体审查汇总
├── brainstorm-signal-tests-review-correctness.md
├── brainstorm-signal-tests-review-statistics.md
└── brainstorm-signal-tests-review-data-handling.md
```

这些文件天然适合 replication ——`scholar-replication` 后面会自动捡起来。

#### 7.2.5 检查（DATA 模式额外两条）

在 MATERIALS 模式四条之外，再核对：

5. **信号检验脚本必须是真 R，不是伪代码。** 打开 `scripts/brainstorm-signal-tests.R`，`head -40` 看看。每个测试都必须包在 `tryCatch()` 里——一个候选失败不能拖垮整轮。
6. **效应量必须用正经包。** 脚本必须用 `effectsize::cohens_d()`、`effectsize::eta_squared()`、`effectsize::cramers_v()`，不能手写公式。

**自检：** 看上面那张信号表。RQ5 的 WEAK 信号意味着“假设死了”吗？不是——它可能只是说“双变量不够，需要协变量”。信号是 Top-10 评分的一个输入，不是判决。

### 7.3 PAPER 模式 —— 从一篇论文起步

适用：**你刚读完一篇论文，想要一份结构化的后续选题菜单**——方法扩展、人群迁移、机制深化、局限解决、计算升级。

PAPER 模式三种触发方式：

```
# (a) 磁盘上的 PDF
> /scholar-brainstorm ~/papers/li-ouyang-hu-2025-digital-divide-aging.pdf

# (b) DOI 字符串
> /scholar-brainstorm 10.1038/s41746-025-02076-1

# (c) 粘贴摘要（直接在对话里贴 "Title: ... Abstract: ..." 块）
> /scholar-brainstorm
> Title: A ten-year analysis of digital divides among older Chinese adults
> Abstract: Using six waves of CFPS we document persistent age-related gaps in [...]
```

#### 7.3.1 技能在做什么

1. **抽取种子论文要素** —— 标题、摘要、核心发现、所用方法、作者承认的局限、作者建议的未来方向、理论框架、人群/语境、数据源。（DOI 走 CrossRef API；PDF 走 `pdftotext`；粘贴摘要直接解析。）
2. **（可选）SciThinker 选题** —— 环境里设了 `HF_TOKEN` 时，技能会调用 HuggingFace 上的 `OpenMOSS-Team/SciThinker-30B`，用结构化提示要求一篇 follow-up 论文的 title + abstract。`HF_TOKEN` 缺失或调用失败时，这步记为 `SKIPPED`，继续走 Claude-only 选题。
3. **Claude 扩展** —— 基于种子要素（+ SciThinker 提案，如有）生成 15–20 个候选 follow-up RQ，覆盖 8 个维度：

```
| 维度         | 策略                                          |
|------------|---------------------------------------------|
| 方法扩展      | 用更强 / 不同的方法回答同一个问题                  |
| 人群迁移      | 同一问题，不同人群或语境                       |
| 机制深化      | 直接检验作者假设的机制                         |
| 局限解决      | 攻克作者承认的某个局限                         |
| 范围扩展      | 推到一个相邻现象                              |
| 反向证伪      | 设计一个能证伪原发现的研究                     |
| 计算升级      | 用 NLP/ML 揭示原方法看不到的模式               |
| SciThinker 提案 | 把 AI 生成的想法在社会科学理论里 ground       |
```

4. **共享流水线** —— 每个候选走文献扫描 → Top-10 短列表 → 五智能体评估组 → 精修 Top-10 → 研究计划概览，与 MATERIALS / DATA 完全一致。

#### 7.3.2 拿 CFPS 数字鸿沟当种子的话会看到什么

如果对 Li, Ouyang, & Hu (2025) 跑 PAPER 模式，可期的 follow-up RQ 例如：

```
#1（机制深化）—— 家户内数字传递（同住青年人）能否削弱 Li 等人指出
   的年龄数字鸿沟？CFPS family-conf + intra-household FE。

#2（人群迁移）—— 同样的"年龄 × 数字排斥"模式在农村流动人口里成立吗？
   户口与年龄叠加。CFPS 流动人口子样本。

#3（局限解决）—— 种子论文承认无法分离世代与年龄。对同一面板用 HAPC
   + Deaton-Paxson bounds。

#4（方法扩展）—— 种子论文用描述趋势。对城乡 Y2 差距跑 Oaxaca-Blinder
   分解，把禀赋部分与系数部分分开。

#5（计算升级）—— 对 CFPS 互联网开放题项跑 STM 主题模型，揭示封闭题
   看不到的使用类型异质性。
```

（数字鸿沟焦点论文实际上正是这么定的位——把 Li 等人当种子，识别第二层 / 制度差距是空白车道。）

#### 7.3.3 写入磁盘的文件（PAPER 模式）

```
output/<slug>/
├── scholar-brainstorm-<slug>-<date>.md          ← 完整报告
├── scholar-brainstorm-<slug>-summary-<date>.md  ← 执行摘要
└── logs/
    ├── process-log-scholar-brainstorm-<date>.md
    └── scithinker-response-<date>.txt           ← 调过 SciThinker 的原始输出
```

#### 7.3.4 检查（PAPER 模式）

四条 MATERIALS 通用检查之外，再加：

5. **与种子的连接。** 每个候选必须明确写出它扩展的是种子的哪个要素（哪条发现？哪条局限？哪条建议方向？）。如果某个候选没法 cite 种子里的具体锚点，那就是幻觉，不是扩展。
6. **SciThinker 落地。** 如果调过 SciThinker，它的提案会被标出来。把它当作种子想法，**不是**成品 RQ——像 Claude 处理它一样：精修、理论化、再打分。

**自检：** PAPER 模式最容易被滥用——很容易拿了榜首 follow-up 就开始写。**别这么做**。把选中的候选送回 `scholar-idea`（§8）和 `scholar-design`（§9）再决定——PAPER 模式是**菜单生成器**，不是设计。

## 8. `scholar-idea` —— 把困惑磨锐

**目标：** 把领域变成具体困惑：机制、范围条件、假设、致命缺陷筛查。

### 8.1 运行

```
> /scholar-idea broad puzzle: "China's digital divide — access converging
  while use intensity persists by hukou, cohort, and gender"
  data: CFPS 2010-2020 long panel
  target: Social Forces
```

### 8.2 真实输出节选（来自 `idea/scholar-idea-...md`）

```markdown
## Step 1 — 困惑

中国 2024 年互联网用户已达 10.7 亿（CNNIC），却仍是分层数字不平等的
教科书案例。第一层接入差距自 2015 年起迅速缩小，但第二层（技能、使用
自主性）和第三层（使用回报）差距似乎扩大，尤其沿 hukou、世代、性别、
教育线分布。

## Step 2 — 候选角度

| # | 框架            | 机制                    | 替代解释          |
|---|----------------|-------------------------|-------------------|
| A | 户口为持久轴   | 制度排序                | 纯 SES 吸收户口  |
| B | 世代即原因     | 出生世代社会化          | 时期效应          |
| C | 家户作为技能单位| 家户内溢出              | 选择              |
| D | 性别×年龄×户口 | 三重惩罚                | 仅可加性          |
| E | 使用回报       | 资本转换 (Bourdieu)     | 回报相同          |

A、B、D 在 CFPS 中可行；E 降级到讨论。

## Step 5 — 假设

H1（户口持久）。控制 X3、X4、地区基础设施后，农业户口降低 Y1 接入概率
和 Y2 周使用小时。Y1 上的户口效应跨波次缩小（接入趋同），Y2 上的户口
效应不缩小（技能-使用分化）。

H2（世代分层）。1985 后出生世代在 Y1 与 Y2 上系统性更高，控制时期与
年龄。在世代内，Y2 的年龄轨迹近乎平坦——鸿沟靠世代替代，不是个人学习。

H3（交叉三重惩罚）。三向交互（农业户口 × 女性 × 1965 年前出生）的
使用强度惩罚超过三个边际效应之和。

H4（家户溢出，次要）。与至少一名"数字原住民"（≥1990 出生）同住，与
年长成员更高的 Y1、Y2 相关。
```

### 8.3 关键观察

- **假设是预先指明的**：H1 既有方向，又有“Y1 缩小但 Y2 不缩小”的微妙性，意味着分析可以**证伪**制度账户，而不只是确证。
- **禁止语言已写明**：备忘里记下禁止的因果语言与描述性设计（“不对户口做因果解释；描述性设计”）。
- **一个假设是高风险的**：H3 是交叉性主张。**现在**就要决定：如果数据显示三重惩罚只是可加，你愿不愿意把这个 null 发出去？（剧透：在我们的运行里 H3 真的是 null，我们把它留在论文里。）

**自检：** 不看文档，能不能用一句话说出每个假设的方向预测？说不出就再磨。

## 8A. `scholar-lit-review-hypothesis` —— 一次性整合文献综述、理论与假设

**目标：** 在一个工作流里完成：摸清现有文献 → 找到未解决的缺口 → 选定能填这个缺口的理论框架 → 指明机制 → 推导可检验假设——直接产出可发表的“文献综述 + 理论”章节。

这个技能**取代**分别跑 `/scholar-lit-review` 和 `/scholar-hypothesis`。在 `/scholar-idea`（§8）之后用最合适。CFPS 数字鸿沟那篇论文里 1,400 字的“理论框架 + 假设”段，就是它写的。

### 8A.1 内部五步逻辑

技能强制单一五步论证——每一步喂下一步，文字不能漂离这条链：

| 步骤 | 内容 | 文字锚点 |
|---|---|---|
| 1 | 文献已**确立**的 | "Prior work has shown X, Y, Z (Author Year)" |
| 2 | 文献仍**未解决**的 | "Yet none of these studies has examined …" |
| 3 | 哪个理论框架**填这个缺口** | 命名理论 + 1–3 篇锚点引用 |
| 4 | 框架预测什么**机制** | 命名了步骤的因果链 |
| 5 | 由机制能推出哪些**假设** | H1–Hn 带方向预测 |

### 8A.2 运行

```
> /scholar-lit-review-hypothesis
   RQ: In CFPS 2010-2020, did hukou/cohort gaps in internet access narrow
       while gaps in weekly use hours persisted?
   target: Social Forces
   anchor theories: layered digital divide; hukou as institutional sorting;
                    cumulative advantage; cohort-as-cause
```

技能跑分层文献检索：

- **Tier 0 —— 知识图谱** —— 跨项目 `scholar-knowledge` 图谱，配置后优先查询
- **Tier 1 —— 本地文献库**（Zotero / Mendeley / BibTeX / EndNote）—— 命中即已验证
- **Tier 2 —— 外部 API** —— CrossRef、Semantic Scholar、OpenAlex、Google Scholar
- **Tier 3 —— WebSearch** —— 仅用于剩余空缺

然后跑**反抄袭 + 主张验证小组**：三个 Task 调度的评估 prompt 并行（originality-auditor、claim-verifier、attribution-analyst —— skill 内部角色，并非 `.claude/agents/` 中的具名 agent），逐句核对 paraphrase 是否过界、效应方向是否与原文一致、引用是否对得上本地库。一致性矩阵附在输出里。

### 8A.3 真实输出（CFPS 运行节选）

下面这段“假设”块技能直接产出，**原封不动**进了最终手稿：

```markdown
## Hypotheses

H1 (Hukou persistence and access-intensity divergence). Net of education,
household income, occupation, and province-level infrastructure, agricultural-
hukou status reduces both the probability of internet access and the weekly
hours of internet use among users. The hukou coefficient on internet access
narrows monotonically across the 2010-2020 panel waves, consistent with
access convergence. The hukou coefficient on weekly internet hours does not
narrow, and may widen, consistent with the institutional-sorting mechanism
producing a durable second-level divide.

H2 (Cohort layering, not within-person learning). Birth cohorts born after
1985 exhibit systematically higher internet access, weekly internet hours,
and use breadth than earlier cohorts, net of period and chronological age.
Within cohort, the within-person age trajectory of weekly internet hours is
approximately flat. Aggregate population-level growth in weekly internet
hours across waves is therefore primarily driven by cohort replacement.

H3 (Intersectional triple penalty). The use-intensity penalty associated
with the joint condition rural-hukou × female × born ≤ 1965 exceeds the
sum of the three additive marginal effects.

H4 (Household spillover, secondary). Co-residence with at least one
digital-native household member (born 1990 or later) is associated with
higher internet access and weekly internet hours for older co-residents,
with the spillover larger for women and rural residents.
```

注意**因果语言校准** —— H1 用 "is associated with" / "reduces the probability of“，不是 ”causes"。这是技能的明确规则：观测设计、未做 IV / RD 识别的假设，必须用关联语言。

### 8A.4 写入磁盘的文件

```
output/<slug>/
├── drafts/scholar-lrh-<slug>-<date>.md             ← 文献综述 + 理论 + 假设（+ .docx/.tex/.pdf）
├── drafts/scholar-lrh-<slug>-<date>.bib            ← 由 /scholar-citation MODE 6b 生成（非人工撰写）
├── logs/
│   ├── process-log-scholar-lit-review-hypothesis-<date>.md
│   └── scholar-search-log-<slug>-<date>.md         ← 每次查询 + 命中数
└── reports/
    ├── source-integrity-panel-<date>.md            ← 三 agent 验证
    ├── source-integrity-originality-<date>.md
    ├── source-integrity-claim-<date>.md
    └── source-integrity-attribution-<date>.md
```

### 8A.5 检查

1. **每句 paraphrase 都必须能追到 `refs.bib` 里的已验证条目。** 打开 source-integrity 面板看哪些句子被标。
2. **每条假设都必须从命名机制推出。** 假设上方没有机制段就是断链。
3. **因果语言审计。** 在草稿里搜 "causes"、"leads to"、"effect of"。观测设计、未做识别的，每一处命中都是修订候选。

**自检：** 在草稿里指一处引用，打开 BibTeX，找得到对应 key 吗？找不到就先跑 `/scholar-citation verify`（§16）再走。

## 8B. `scholar-conceptual` —— 造理论“对象”，不是写理论文字

**目标：** 产出一篇论文真正立足的*理论对象*——类型学、机制链、多层次框架、范围条件、过程模型——并把它们渲染成发表级图（TikZ → PDF，Mermaid 作 fallback）。

这**不是**假设推导（`/scholar-hypothesis`），也**不是**识别（`/scholar-causal`）。`scholar-conceptual` 在*理论建构*层面：理论**由什么构成**？这些部件**怎么连起来**？

### 8B.1 两种模式

| 模式 | 触发 | 输出 |
|---|---|---|
| **THEORIZE** | "theorize"、"build theory"、"construct framework"、"synthesize"、"typology" | 3–5 页备忘：命名定义、范围条件、机制、对手解释、局限 |
| **DIAGRAM** | "diagram"、"figure"、"mechanism diagram"、"concept map"、"tikz" | 独立 `.tex` (TikZ) 编译为 `.pdf`；可选 `.mmd`/`.svg`/`.png` Mermaid 版 |

THEORIZE 进一步把任务分八类——类型学构建（Lazarsfeld property-space）、过程理论化、机制说明（Coleman's boat / Hedström DBO）、范围条件映射、多层次模型、abductive 异常 → 解释、综合框架、概念澄清。

### 8B.2 运行（数字鸿沟例子）

```
> /scholar-conceptual build mechanism model: access convergence,
                    persistent intensive-use stratification,
                    hukou and cohort sorting
                    target: Social Forces
                    diagram type: Coleman's boat
```

技能写出：

- **`output/<slug>/theory/mechanism-memo-<date>.md`** —— 1,500 字备忘，命名每个机制步骤（制度排序 → 基础设施差异暴露 → 技能形成 → 使用强度分层），明确列出对手解释，逐条箭头给出反证证据。
- **`output/<slug>/figures/fig-mechanism-coleman.tex`** —— Coleman's-boat 图的 TikZ 源（宏观条件 → 个体情境 → 个体行为 → 宏观结果）。
- **`output/<slug>/figures/fig-mechanism-coleman.pdf`** —— 编译后的矢量 PDF，可直接放进 LaTeX。
- **`output/<slug>/figures/fig-mechanism-coleman.mmd` / `.svg`** —— Mermaid fallback（迭代时渲染快）。

### 8B.3 编译后的真图 —— 我们 CFPS 案例的 Coleman's boat

技能产出可直接编译的 TikZ，`latexmk` / `xelatex` 把它编成独立 PDF，可直接拖进手稿。下面是这条技能在 digital-divide 项目上**真实编译出来**的图 —— 不是重画的示意图：

<figure class="hb-figure">
<img src="/images/fig-mechanism-coleman.png" loading="lazy" alt="Coleman's boat mechanism: the Hukou system (macro) links to the population-level use-intensity gap (macro) via differential digital infrastructure exposure and differential skill conversion (micro), with rival explanations listed as falsifiers.">
<figcaption>图 8B.1 —— CFPS 2010–2020 中农村-城市使用强度差距（Y2）的 Coleman's boat 机制图。粗的宏观→宏观箭头是论文描述层面观察到的总体关联；三条橙色的微观层箭头描出我们主张的"制度分层"机制，下方的可证伪假说列在底部作为稳健性检验的对应清单。</figcaption>
</figure>

下面是技能写出的 TikZ 源（节选 —— 完整文件在 `output/theory/fig-mechanism-coleman.tex`）：

```latex
\begin{tikzpicture}[
  box/.style={draw=primary, rounded corners=3pt,
              minimum width=3.6cm, minimum height=1.1cm,
              align=center, font=\small, fill=white},
  macrobox/.style={box, fill=lightbg, font=\small\bfseries},
  arrow/.style={-{Stealth[length=7pt]}, primary},
  microarrow/.style={-{Stealth[length=7pt]}, accent},
  label/.style={font=\scriptsize\itshape, muted}]

% 宏观层
\node[macrobox] (M1) at (0, 3) {Hukou system\\(institutional sorting)};
\node[macrobox] (M2) at (10, 3) {Population-level\\use-intensity gap (Y2)};

% 微观层
\node[box] (m1) at (2.6, 0) {Differential digital\\infrastructure exposure};
\node[box] (m2) at (7.4, 0) {Differential\\skill conversion};

% Coleman 船的四条腿
\draw[arrow]      (M1) -- (M2) node[midway, above, label] {Observed gap (descriptive)};
\draw[microarrow] (M1.south) -- (m1.north) node[midway, left,  label] {(1) Situational};
\draw[microarrow] (m1) -- (m2) node[midway, below, label] {(2) Action-formation};
\draw[microarrow] (m2.north) -- (M2.south) node[midway, right, label] {(3) Transformational};
\end{tikzpicture}
```

技能同时写一个 figure caption 块（可以直接贴在手稿图下）以及一份 `Rival explanations to test:` 检查清单（编译图底部可见的那段）—— 这是论文稳健性章节必须回应的经验性可证伪点。

### 8B.4 八种可渲染的图

| 类型 | 适用 | 引擎 |
|---|---|---|
| 机制图（Coleman's boat） | 因果链、中介路径 | TikZ |
| 多层次模型 | 宏-中-微、跨层效应 | TikZ |
| 类型学矩阵 | 2×2 / 2×3 property-space | TikZ 或 `ggplot2 + geom_tile` |
| 过程模型 | 时间阶段、相位转换 | TikZ 或 Mermaid |
| 概念图 | 理论概念之间的关系 | Mermaid 或 Graphviz |
| 反馈环 | 累积优势、强化 / 平衡 | TikZ |
| 范围边界 | 理论适用 vs. 不适用 | TikZ（Venn / 嵌套矩形） |
| 理论综合 | 多个理论如何连接 | TikZ 或 Mermaid |

### 8B.5 检查

- **每条箭头都要有标签的机制。** 打开图，无标签的箭头是装饰，不是理论。
- **每个 box 都要有反证。** 备忘里要写：什么样的观察会削弱这个 box / 这条箭头。学员说不出“什么证据能证伪这条箭头”——这条就还没成熟。

**自检：** 把图给一个没看备忘的同事，让他从图里复述出机制故事。复述不出来，说明图过度装饰、信息不足——加标签重做。

## 8C. `scholar-knowledge` —— 跨项目记忆层

**目标：** 维护**单一、用户作用域、跨项目**的知识图谱：你 ingest 过的每篇论文、抽取过的每条发现、记下的每条方法、标过的每条论文-论文关系，都能在下一项目里复用。它就是**让智能体不再每次重新发现同一片文献**的那一层。

这是技能套件里**最被低估却最有价值**的一个。审计语料里，CFPS 数字鸿沟、CFPS 户口-婚姻、十几个其它项目都在同一个智识邻域里——Wu & Treiman 2004、Xie & Jin 2015、van Deursen & Helsper 2015、DiMaggio et al. 2004 ……。没有 `scholar-knowledge` 时，每个项目从零开始。有了它，ingest 是一次性投资，**永远在还利息**。

### 8C.0 SELECT 的三条路 —— 为什么用 wiki，而不只是 RAG

把*对的*文本送进模型窗口（也就是"SELECT"这一步），有三种截然不同的策略，而 `scholar-knowledge` 是第三种：

- **RAG** —— 把语料切块、做 embedding，查询时按向量相似度取回最近的 top-*K* 块。快、可扩展，但取回的是按*表面相似度*排序的**不透明片段**；源文件一改，索引就过期；而且你很难读出某个块*为什么*被选中。
- **智能体式搜索（agentic search）** —— 没有索引；智能体在循环里 `grep` 并直接读活文件（Claude Code 读你的仓库就是这么干的）。永远是最新、完全可审计，但受限于少数几次搜索够得着的范围，而且每次会话都要从头再读一遍。
- **知识 wiki（"LLM-wiki"路线）** —— 模型把每篇源文献*读一次*，抽取发现、机制与关系，写成**人类可读、互相链接的 markdown wiki**。要回答问题时，它读 index 页、顺着 `[[链接]]` 走到真正相关的那几页。这正是 `/scholar-knowledge compile` 和 `ask` 做的事。

对于一个你会*反复回来查*的语料，wiki 为什么可能胜过 RAG：*综合是预先算好的*（主题综述、`contradictions.md`、`gaps.md`），而不是每次查询都重新推导一遍；关系是*可遍历的显式链接*（`extends`、`contradicts`、`same-dataset`），不是隐含的向量邻居；它*就是 markdown* —— 可审计、可编辑，不需要 embedding 模型、也不需要向量库；而且它会*滚雪球* —— 你把自己的产出 file 回去，于是第 5 篇论文站在第 1–4 篇的肩膀上。代价是：抽取是*前期一次性投入*且有损（wiki 是模型对源文献的*阅读*，不是源文献本身 —— 所以 `raw/` 会保留原件），而且 wiki 必须保持最新（由 LLM 维护，你几乎不用手动改）。这就是 Andrej Karpathy 的"LLM wiki"想法：模型自己写、自己维护这个知识库，你把产出 file 回去，让它为将来的查询变得更好。

三者是**互补，不是对手**。把 wiki 当作持久记忆，把活的检索器（OpenAlex、Zotero）包成 MCP *工具*来延伸触达（Lab 3 §4b），让智能体自己决定该伸手去拿哪一个。想看完整机制 —— ingest → 图谱 → compile → 导航 —— 只用约 250 行零依赖 Python，跑一下 Day 3 的 demo：

```bash
cd demo/day3-claude-code/llm-wiki
python3 build_wiki.py     # 7 篇论文 -> 图谱 -> 34 个互链 wiki 页
python3 ask.py "why doesn't closing the access gap close the divide?"
```

`ask.py` 会打印出确切的导航路径（`index.md → topics/… → concepts/… → papers/…`），把它与 RAG 不透明的 top-*K* 之间的差别摆到明面上。

### 8C.1 文件长什么样

```
~/.claude/scholar-knowledge/                （可用 $SCHOLAR_KNOWLEDGE_DIR 覆盖）
├── papers.ndjson         ← 每行一个 JSON，描述一篇论文（含抽取出的丰富内容）
├── concepts.ndjson       ← 命名概念、理论、机制
├── edges.ndjson          ← 论文间关系（cites、contradicts、extends ……）
├── meta.json
└── raw/                  ← **append-only** 原始档案
    ├── pdfs/             ← 软链到 Zotero PDF（不复制大文件）
    ├── abstracts/        ← 抽取的文本
    ├── api-responses/    ← 原始 CrossRef / Semantic Scholar JSON
    ├── web/              ← 抓取的预印本、NBER WP、博客
    └── images/           ← 从 PDF 抽出的图（每篇一个子目录）
```

一个 paper 节点（真实 schema，简化版）：

```json
{
  "id": "fiel-zhang-2017",
  "doi": "10.1007/s13524-017-0632-9",
  "title": "Three Dimensions of Change in School Segregation: A Grade-Period-Cohort Analysis",
  "authors": ["Fiel, Jeremy E.", "Zhang, Yongjun"],
  "year": 2017,
  "journal": "American Sociological Review",
  "findings": ["School segregation decreased along racial lines but increased along socioeconomic lines between 1999 and 2010."],
  "mechanisms": ["compositional change (demographic shifts)"],
  "theories": [{"name": "spatial assimilation", "role": "tests"}],
  "methods": ["decomposition analysis", "multilevel models"],
  "populations": ["K-12 students in US public schools"],
  "data_sources": ["Common Core of Data (CCD)"],
  "limitations": ["Data limited to public schools"],
  "future_directions": ["Within-district heterogeneity at the classroom level"],
  "projects": ["segregation-paper-2026", "digital-divide-china-cfps"],
  "raw_path": "abstracts/fiel-zhang-2017.txt"
}
```

重点是 `findings`、`mechanisms`、`methods`、`limitations`、`future_directions`——**你的文献管理器不存这些**，可你天天要用。

边长这样：

| 谓词 | 方向 | 例子 |
|---|---|---|
| `cites` | A → B | Xie & Jin 2015 → Wu & Treiman 2004 |
| `contradicts` | A ↔ B | Cui 2024 ↔ Cheng & Selden 1994 |
| `extends` | A → B | 本文 → Li, Ouyang, & Hu 2025 |
| `replicates` | A → B | 复制研究 → 原文 |
| `uses-method` | A → B | 本文 → Oaxaca & Ransom 1994 |
| `uses-theory` | A → B | 本文 → DiMaggio et al. 2004 |
| `same-dataset` | A ↔ B | 两篇用同一份 CFPS 面板的论文 |

### 8C.2 八种模式 —— 具体命令

| 模式 | 触发词 | 做什么 |
|---|---|---|
| **INGEST** | `ingest`、`add`、`import`、`extract` | 从 Zotero / PDF / DOI / URL / 文献综述文件 / 技能输出导入；抽取发现/机制/等等；归档原始源 |
| **SEARCH** | `search`、`find`、`query`、`what do we know about` | 对 papers + concepts + edges 做布尔 / 关键词 / 正则检索 |
| **RELATE** | `relate`、`link`、`connect`、`contradicts`、`extends` | 添加或查看论文间关系 |
| **STATUS** | `status`、`stats`、`coverage`、`dashboard` | 图谱统计：论文数、Top 理论、按主题覆盖度 |
| **EXPORT** | `export`、`subset`、`for project` | 项目作用域子集（例如，只导出标了 `digital-divide-china-cfps` 的论文） |
| **COMPILE** | `compile`、`build wiki`、`wiki` | 从图谱生成 Obsidian 风格 markdown wiki |
| **ASK** | `ask`、`why`、`how do`、`compare`、`summarize` | 跨 wiki 回答复杂研究问题 |
| **RE-EXTRACT** | `re-extract`、`refresh`、`enrich` | 用更新后的 schema 重新抽取（例如，把 abstract-only 论文升级为全 PDF；或加新字段） |

#### 模式 1 —— INGEST：从 Zotero 批量导入

```
> /scholar-knowledge ingest from zotero collection "digital divide"
> /scholar-knowledge ingest from zotero tag "hukou"
> /scholar-knowledge ingest from zotero keyword "second-level digital divide" 30
```

对每篇命中：

1. 读 Zotero SQLite 拿到书目元数据
2. 把 PDF 软链（不复制）到 `raw/pdfs/<slug>.pdf`
3. `pdftotext` 抽前 400 行
4. 装了 `poppler` 时还可以 `pdfimages` 抽图
5. 抽 findings / mechanisms / theories / methods / populations / data sources / limitations / future directions / key quotes（带页码，如有）
6. 把 `paper` 节点 append 到 `papers.ndjson`
7. 新理论 / 新机制 append 到 `concepts.ndjson`
8. 按 DOI / 标题 hash 去重——重复 ingest 是幂等的

#### 模式 1 —— INGEST：从 PDF / DOI / URL / 自己作品

```
> /scholar-knowledge ingest from pdf ~/papers/li-ouyang-hu-2025.pdf
> /scholar-knowledge ingest from doi 10.1038/s41746-025-02076-1
> /scholar-knowledge ingest from url https://www.nber.org/papers/w29234
> /scholar-knowledge ingest from output output/digital-divide-china-cfps/drafts/manuscript-final-2026-05-04.md
```

最后一条——`from output`——是**反馈闭环**。每写完一篇论文，把自己的论文 ingest 回图谱。论文类型变成 `"own_work"`，发现就能在下一个项目里被检索到。

#### 模式 2 —— SEARCH

```
> /scholar-knowledge search "second-level digital divide China"
> /scholar-knowledge search papers using-method "Oaxaca-Blinder"
> /scholar-knowledge search papers contradicts spatial-assimilation
```

返回论文 ID、题目、相关性排序、每条命中一句解释。它直接喂 `scholar-lit-review-hypothesis`（§8A）—— lit-review 技能查外部 API **之前**先读 `papers.ndjson`。

#### 模式 4 —— STATUS（仪表盘）

```
> /scholar-knowledge status
```

真实输出：

```
Knowledge graph at ~/.claude/scholar-knowledge
  Papers:   1,142
  Concepts: 287
  Edges:    3,901
  Raw archive: 4.2 GB across 1,142 PDFs and 318 web fetches

Top theories (by paper count):
  1. cumulative advantage / Matthew effect            (87 papers)
  2. spatial assimilation                             (54 papers)
  3. layered (three-level) digital divide             (41 papers)
  4. hukou as institutional sorting                   (33 papers)
  5. second-demographic transition                    (29 papers)

Coverage gaps (theories with <3 papers):
  - distributed cognition + digital practice (1 paper — extend)
  - intersectional algorithmic harm           (2 papers — extend)
  - capability approach × digital inclusion   (0 papers — gap)

Project tags:
  digital-divide-china-cfps    (76 papers)
  hukou-marriage-cfps           (94 papers)
  segregation-paper-2026       (108 papers)
  …
```

#### 模式 6 —— COMPILE：把图谱编译成 Obsidian wiki

```
> /scholar-knowledge compile
```

在 `~/.claude/scholar-knowledge/wiki/` 产出一份完整链接的 markdown wiki：每篇论文一页、每个理论 / 机制一页、`[[wiki-link]]` 互相引用。Obsidian（或任意 markdown 阅读器）打开后图谱视图可浏览。每次 ingest 之后跑一次。

#### 模式 7 —— ASK：跨图谱问研究问题

```
> /scholar-knowledge ask what are the main theories of the second-level digital divide?
> /scholar-knowledge ask compare the mechanisms in van Deursen & Helsper 2015 vs Hargittai 2002
> /scholar-knowledge ask which CFPS papers in my graph use Oaxaca-Blinder decomposition?
```

技能读已编译的 wiki，回答时带论文级引用。**所有主张都被你 ingest 过的内容约束住**，幻觉空间被锁死。

#### 模式 8 —— RE-EXTRACT：升级 schema

给 paper 节点加新字段（比如 "data-availability statement“ 或 ”preregistration link"）后跑：

```
> /scholar-knowledge re-extract all abstract_only
> /scholar-knowledge re-extract field=data_availability
```

技能遍历 `raw/`，按更新后的 schema 重新抽取——**不**重新抓网络。这正是 raw 档案 **append-only** 的意义：schema 可以变，源不能变。

### 8C.3 这件事对 CFPS 工作坊为什么重要

工作坊流水线里，`scholar-lit-review-hypothesis`（§8A）**先**查 `papers.ndjson`，再查 WebSearch。如果你已经 ingest 过 Wu & Treiman 2004、Xie & Jin 2015、van Deursen & Helsper 2015 等，lit-review 直接拿全字段已验证书目去引用，不会留下 "[CITATION NEEDED]" 占位。`scholar-citation verify`（§16）也一样——本地命中是 Tier 1，免费且即时。

正确的节奏：

```
每写完一篇论文：
   /scholar-knowledge ingest from output drafts/manuscript-final-...md
   /scholar-knowledge compile

每开一个新项目：
   /scholar-knowledge ask what do I already know about <topic>?
   /scholar-knowledge export for project <new-slug>
```

### 8C.4 检查

- **`raw/` 是 append-only。** 永远不要 `rm`。审计轨迹靠它。
- **边数应该是概念数的 ~10 倍。** 400 篇论文却只有 12 条边——你 ingest 了，但没连——跑 `relate` 模式。
- **重抽很便宜。** 加新 schema 字段了？`re-extract` 是朋友；不要从源重新 ingest。

**自检：** 每月跑一次 `/scholar-knowledge status`。"Coverage gaps" 里出现你正引用的理论——下次写综述前先 ingest 5–10 篇锚点论文。

### 8C.5 Obsidian wiki —— 安装、配置、浏览

`/scholar-knowledge compile` 在 `~/.claude/scholar-knowledge/wiki/` 生成一份 [Obsidian](https://obsidian.md) 兼容 vault。Obsidian 免费、本地优先，是真正能让你**读**和**导航**这张图的最顺手工具。本节走一遍技能预期的配置。

#### 8C.5.1 `compile` 写出什么

```
~/.claude/scholar-knowledge/wiki/
├── index.md                ← 仪表盘：统计、近期 ingest、快捷链接
├── knowledge-map.png       ← 渲染好的网络图（如生成）
├── contradictions.md       ← 争议发现（图中带 contradicts 边的论文）
├── gaps.md                 ← 研究空白与未被填的 future-direction
├── papers/                 ← 每篇论文一页
│   ├── fiel-zhang-2017.md
│   ├── li-ouyang-hu-2025.md
│   ├── van-deursen-helsper-2015.md
│   └── …                                       （通常是几百个文件）
├── concepts/               ← 每个理论 / 方法 / 机制一页
│   ├── spatial-assimilation.md
│   ├── layered-digital-divide.md
│   ├── oaxaca-blinder-decomposition.md
│   └── hukou-as-institutional-sorting.md
├── topics/                 ← 自动聚类的主题页
│   ├── digital-inequality-china.md
│   └── residential-segregation.md
└── answers/                ← Q&A 存档（每次 /scholar-knowledge ask 都增加一条）
    └── second-level-digital-divide-mechanisms-2026-05-08.md
```

一篇论文页（`papers/li-ouyang-hu-2025.md`）渲染成这样：

```markdown
# Li, Ouyang & Hu (2025) — Ten-Year Analysis of Digital Divides Among Older Chinese Adults

**Journal:** npj Digital Medicine
**DOI:** 10.1038/s41746-025-02076-1
**Data:** [[CFPS]] 2010–2020

## Findings
- Persistent age-related gap in healthy-aging outcomes attributable to digital exclusion.
- Gap does not narrow across the decade despite access growth.

## Mechanisms
- [[skill-conversion]] — older cohorts' lower marginal returns to use.

## Theories used
- [[layered-digital-divide]]  (role: applies)
- [[cumulative-advantage]]    (role: extends)

## Methods
- [[OLS-with-fixed-effects]]
- [[descriptive-decomposition]]

## Limitations (per authors)
- Cannot separate cohort from age in single panel — [[APC-identification]] is non-identified without restriction.

## Future directions (per authors)
- Within-household digital transmission — see [[household-spillover]].

## Edges
- This paper **uses-theory** [[van-deursen-helsper-2015]]
- This paper **extends** [[ren-zhu-2024]]
- This paper is **cited-by** [[zhang-2026-digital-divide-china-cfps]]   (own-work)

---
*Ingested: 2026-04-12 from Zotero. Raw: `raw/pdfs/li-ouyang-hu-2025.pdf`.*
```

一个概念页（`concepts/layered-digital-divide.md`）：

```markdown
# Layered (Three-Level) Digital Divide

A theoretical framework distinguishing access (Level 1), skill / use intensity
(Level 2), and conversion of online activity into offline returns (Level 3).

## Anchor papers
- [[dimaggio-hargittai-celeste-shafer-2004]] — original five-dimension formulation
- [[hargittai-2002]] — coined "second-level digital divide"
- [[van-deursen-helsper-2015]] — named the third level
- [[robinson-et-al-2015]] — life-course / gender / race consolidation

## Papers using this framework      (41 in graph)
- [[li-ouyang-hu-2025]]
- [[ren-zhu-2024]]
- [[zhang-2026-digital-divide-china-cfps]]   (own-work)
- …

## Mechanisms
- [[skill-formation]]
- [[content-sorting]]
- [[opportunity-matching]]

## Empirical predictions in this graph
- Access gaps narrow as penetration saturates.
- Use-intensity gaps **persist or widen** under cumulative advantage.
- Returns gaps depend on cultural and economic capital.

## Contradictory evidence (in graph)
- [[zhao-et-al-2022]] — finds narrowing intensity gap among rural Chinese students under online learning.
```

`[[双方括号]]` 是 **wiki-link**——Obsidian 渲染成可点链接，`Cmd+Click` 跳转，**Backlinks** 侧栏会自动告诉每页“哪些其他页链向了我”，你不用手工维护反向指针。

#### 8C.5.2 安装 Obsidian、打开 vault

```bash
# macOS
$ brew install --cask obsidian

# Linux（从 obsidian.md 下 AppImage）
$ # 下载 Obsidian-1.x.AppImage、chmod +x、运行

# Windows（WSL 学员：在 Windows 侧装 Obsidian，指向 WSL 路径）
```

打开 vault：

1. 启动 Obsidian
2. 点击 **Open folder as vault**
3. 按 `Cmd+Shift+G`（macOS）或 `Ctrl+L`（Linux），粘贴：

   ```
   ~/.claude/scholar-knowledge/wiki
   ```

4. 确认。Obsidian 索引 vault——1,000 篇论文图谱首次大约 30–60 秒。

便利软链：

```bash
$ ln -s ~/.claude/scholar-knowledge/wiki ~/Desktop/scholar-wiki
```

之后从 Finder 直接打开 `~/Desktop/scholar-wiki` 就行。

#### 8C.5.3 推荐 Obsidian 设置

**Files & Links：**

- **Detect all file extensions** → ON
- **Default location for new notes** → "In the folder specified below" → `answers/`
- **Use [[Wikilinks]]** → ON（默认）

**Editor：**

- **Readable line length** → ON

**核心插件**（Settings → Core plugins，全部开启）：

- **Graph view** (`Cmd+G`) —— papers ↔ concepts ↔ topics 的可视化网络
- **Backlinks** —— 每页侧栏显示“谁 `[[…]]` 引用了我”
- **Outgoing links** —— 每页侧栏显示“我链向了哪些”
- **Quick switcher** (`Cmd+O`) —— 输入页名跳转
- **Search** (`Cmd+Shift+F`) —— 全文搜索整个 vault
- **Tags** —— 你给页面加 `#topic/segregation` 之类的话用

**社区插件**（Settings → Community plugins → Browse）：

- **Dataview** —— 把 wiki 当数据库查询：
  ```dataview
  TABLE journal, year FROM "papers"
  WHERE contains(theories, "layered-digital-divide") AND year >= 2020
  SORT year DESC
  ```
  实时渲染：你图谱里 2020 年后用 layered framework 的所有论文。
- **Graph Analysis** —— 在 wiki 图上算 centrality、clustering、betweenness
- **Breadcrumbs** —— paper → concept → topic 层级导航
- **Calendar** —— 按 ingest 日期看论文

#### 8C.5.4 Graph View 配置

`Cmd+G` 打开。默认视图无差别，按下面配：

**Filters 面板：**
- **Tags** —— 按标签显示 / 隐藏
- **Orphans** 开关 —— 切到只看孤立论文（`relate` 模式候选）

**Groups（按节点类型上色）** —— 点 "+ Add group" 五次：

| 颜色 | 过滤表达式 | 高亮什么 |
|---|---|---|
| 蓝 | `path:papers/` | 单篇论文页 |
| 红 | `path:concepts/` | 理论、方法、机制 |
| 绿 | `path:topics/` | 自动聚类主题页 |
| 黄 | `path:answers/` | `/scholar-knowledge ask` 的输出 |
| 紫 | `file:contradictions OR file:gaps OR file:index` | 聚合 / 仪表盘页 |

**Display 面板：**

- **Node size** → "By number of links"——突出连接最多的论文（通常是子领域的锚点引用）
- **Arrow** → ON——`[[…]]` 引用方向可见
- **Line thickness** → "By number of connections"

效果：密集红簇是有大量支持论文的理论；密集蓝簇是子领域；连两簇的桥节点是*整合性*论文，最值得仔细读。

#### 8C.5.5 四种浏览模式

**(a) 浏览研究地图。**

打开 `index.md`。点一个主题（如 `[[digital-inequality-china]]`），看到这个主题下的论文与概念清单。点任意论文看 findings、theories、methods。**Backlinks** 侧栏告诉你谁引用 / 扩展了它。

**(b) 找连接。**

`Cmd+G` 打开 Graph View。在搜索框里输概念名（如 `hukou-as-institutional-sorting`）。它在图里高亮，邻居就是用了这概念的论文。注意找*桥节点*——连接两个原本独立簇的节点。这些论文最可能给你一个新颖的框架。

**(c) 在 wiki 上问问题。**

在 Claude Code 里跑 `/scholar-knowledge ask <问题>`。答案存到 `wiki/answers/<问题-slug>-<日期>.md`，并附上它咨询过的所有 wiki 页的引用。在 Obsidian 里打开答案文件——**Backlinks** 侧栏列出所有“喂”过这个答案的论文。一年之后，`answers/` 文件夹本身就是一份可搜索的 Q&A 档案。

**(d) 跟踪研究进展。**

- `wiki/gaps.md` —— 图谱说哪些方向你还没研究（`STATUS` 模式里覆盖度低）
- `wiki/contradictions.md` —— 有争议的发现（图里有 `contradicts` 边）
- `wiki/answers/` —— 你已经探索过的问题
- Graph View —— 密集簇是研究充分的领域，稀疏区是空白

#### 8C.5.6 让 wiki 保持最新

wiki 自动更新：

- **每次 ingest 之后** —— paper 页、concept 页、`index.md` 只对新条目增量重生。
- **全量重建** —— 跑 `/scholar-knowledge compile full` 重生主题聚类、`contradictions.md`、`gaps.md`、可视化。**每月一次**或大批 ingest 之后跑。
- **手工编辑** —— 你*可以*手改某页（比如在 Findings 段加私人笔记），增量重建会保留。但**全量重建可能覆盖**——想留永久私注，建一个独立的 `notes/` 文件夹自己管，别写在自动生成页里。

**自检：** 在 Obsidian → Graph View 中过滤到当前项目的论文（`path:papers/` + 项目标签）。看到的簇就是你*实际拥有*的文献。`STATUS` 模式标过 "Coverage gap" 而这个簇里又看不到的——那就是你下一次 ingest 应该瞄准的方向。

## 8D. `scholar-causal` —— 有意识地挑一个识别策略

**目标：** 在写设计蓝图之前，先决定这个问题是不是因果问题；如果是，再决定数据到底支持十四种识别策略中的哪一种。本技能位于 `/scholar-hypothesis` 与 `/scholar-design` 之间，是你**把要捍卫的假设写下来、提交在案**的地方。

最近一次更新大幅拓宽了它的覆盖面。早期版本只处理 OLS、DiD、RD、IV、FE、matching、合成控制。现在的版本覆盖**十四种识别策略**，每一种都自带假设、诊断、**R 与 Stata 代码**、以及一份期刊级的写作模板：

1. **OLS** 在 selection-on-observables 下（配 Oster δ）。
2. **2×2 双重差分。**
3. **断点回归** —— Sharp 与 Fuzzy。
4. **工具变量 / 2SLS。**
5. **面板固定效应（TWFE）。**
6. **匹配 / 重加权** —— PSM、CEM、IPW、doubly robust。
7. **合成控制 / SynthDiD。**
8. **因果中介（ACME）** 在序列可忽略性下。
9. **交错 DiD** —— Callaway-Sant'Anna、Sun-Abraham、de Chaisemartin-D'Haultfœuille、Borusyak-Jaravel-Spiess（附一份可直接跑的 CS 工作流模板 `references/did-cs-workflow.R`）。
10. **Double Machine Learning** 与 **causal forests**，用于高维混杂。
11. **Bunching estimation**，在 kink/notch 处。
12. **Shift-share / Bartik IV**，地方层面对总量冲击的暴露。
13. **分布与分位数方法** —— 分位数回归、RIF-OLS、changes-in-changes。
14. **析因 DiD（Factorial DiD, FDID）** —— 用于全体同时暴露、没有干净对照组、但存在事件前基线因子 G 的情形；区分效应修饰与因果调节，配有可运行的工作流模板 `references/fdid-workflow.R`。

### 8D.1 运行

```
> /scholar-causal 农业户口对每周上网时长的效应，
                  CFPS 2010-2020 面板；候选混杂：
                  家庭收入、教育、父母职业、村基础设施
```

技能开场会问三件事：（1）**因果问题**（X 对 Y 的效应）；（2）**数据结构**（截面、面板、自然实验）；（3）**候选混杂与机制**。下游的一切都取决于这三个回答。

### 8D.2 技能产出什么

一次典型运行会在项目目录里写下四份产物：

```
design/
  ├─ causal-dag.tex             # dagitty + TikZ DAG，含调整集
  ├─ identification-memo.md     # 选哪个策略、为什么、假设是什么
  ├─ diagnostic_plan.json       # Tier 1：始终生成 —— 设计前要跑的检查清单
  └─ sensitivity-registry.md    # Oster δ / E-value / HonestDiD / Rosenbaum / Manski
logs/process-log-scholar-causal-<日期>.md
```

**identification-memo.md** 是最关键的一份。它命名所选策略，按“估计对象 → 识别假设 → 估计量 → 威胁”四步走，并列出**禁止主张**清单 —— 这份清单后续会被 `scholar-write`、`scholar-verify`、`scholar-polish` 拿去强制执行。（CFPS 流水线之所以能在 Abstract 用 "reduces“ 而 Methods 只允许 ”is associated with" 时把它拦下来，靠的就是这个机制。）

### 8D.3 方法选择决策表

技能内置一张决策表，agent 会牵着你过一遍。压缩版本：

| 数据结构 / 变异来源 | 核心假设 | 推荐策略 |
| ------------------- | -------- | -------- |
| RCT（随机分配） | SUTVA + 依从性 | OLS / ITT / LATE |
| 截面 + 丰富控制变量 | CIA / unconfoundedness | OLS + Oster δ, matching |
| 高维混杂、大 N | CIA | DML / causal forests |
| 外生冲击、两期 | 平行趋势 | 2×2 DiD |
| 交错政策采纳 | 平行趋势、避免“禁忌比较” | CS / SA / dCDH / BJS |
| 阈值型分配 | 潜在结果连续 | Sharp / Fuzzy RD |
| 可信工具变量 | 排他性 + 相关性 | IV / 2SLS |
| 面板数据 | 无时变混杂 | 面板 FE |
| 无工具变量、观测数据 | 重叠 + unconfoundedness | Matching / IPW / DR |
| 处理单位少、前期长 | 前期拟合 | Synth / SynthDiD |
| 机制 / 中介问题 | Sequential ignorability | 因果中介 |
| Kink / notch 处的聚集 | 反事实密度平滑 | Bunching estimation |
| 地方暴露于总量冲击 | 冲击外生 OR 份额外生 | Shift-share / Bartik IV |
| 分布异质性 | 分位数特异假设 | Quantile / RIF-OLS / CiC |
| 全体同时暴露事件 + 基线因子 G | 析因平行趋势 | 析因 DiD（FDID） |

### 8D.4 敏感性分析套件

挑出策略只完成一半工作。技能还会写一份**敏感性登记表**，把稳健性检查**在你看到结果之前**就锁定：

- **Oster (2019) δ** —— 用于 selection-on-observables 下的 OLS。
- **E-values (VanderWeele & Ding 2017)** —— 把效应“解释干净”所需的最小未观测混杂强度。
- **Rosenbaum bounds** —— 匹配估计量对隐藏偏倚的敏感性。
- **HonestDiD (Rambachan & Roth 2023)** —— 在有限的平行趋势违反下做边界推断。
- **Manski bounds** —— 弱化假设下的部分识别。
- **安慰剂 / 证伪检验** —— 处理前结果、永远未处理组的引领项、时间安慰剂。
- **溢出敏感性** —— 在传染或干扰下违反 SUTVA。
- **Specification curve / multiverse** —— 把所有合理的设定都排出来。

### 8D.5 Tier 1 与 Tier 2 —— 哪些真的会跑你的数据

技能分两层执行。**Tier 1 始终生成 `diagnostic_plan.json`** —— 一份机器可读的检查清单，规定设计锁定前要跑哪些诊断。**Tier 2 默认关，需要显式打开**，直接执行少量预设计诊断：

- **面板预览** 用 `panelview` + `fect` —— 检查处理时序与前趋势。
- **合成控制预览** 用 `gsynth`（Xu 2017）—— 评估 synth / SynthDiD 在你案例上的可行性。
- **交互效应诊断** 用 `interflex`（Hainmueller, Mummolo, Xu 2019）—— 看你的调节变量到底是不是线性的。
- **析因 DiD 预览** 用 `fdid`（Xu, Zhao & Ding 2026）—— 用于交叉处理 / 析因 DiD 设计。

Tier 2 受闸门控制：你必须在提示词里**明确写**「在这份数据上跑诊断」。Tier 2 **不会**估计焦点效应、不会拟合最终模型、不会产出会进论文的数字。它产出的诊断图，是用来辅助 §9（`scholar-design`）里你要提交的那个选择。

### 8D.6 为什么 CFPS 工作坊故意绕开 scholar-causal

本手册里的数字鸿沟案例**故意**不是一个因果设计。户口出生时分配、几乎不变；没有可操纵的“处理”。我们既没有工具变量，也没有断点。正确的做法 —— 也是工作坊演示的做法 —— 是**拒绝采用因果识别策略**，改写一份**描述性/分解设计**。在那种情况下 `scholar-causal` 仍然有用：它产出的 DAG 论证了你的协变量调整集，并在 identification memo 里盖上 `causal_status: descriptive` 戳记，下游技能据此强制执行正确的语言上限。

如果你的项目**确有**因果杠杆 —— CCT 风格的 RCT、政策冲击、断点、可信的 IV —— 项目就从 `scholar-causal` 开局，*然后*再跑 `scholar-design`。决策的是策略；纪律是在分析跑起来之前，把假设写下来。

### 8D.7 自检

进入 §9 之前，打开三个产物各问自己一句：

- `causal-dag.tex` —— 调整集够不够？DAG 漏没漏 back-door 路径？
- `identification-memo.md` —— 一个敌意审稿人能不能把每条假设都打掉？其中是否有一条经验上可检验？
- `sensitivity-registry.md` —— 焦点效应若能挺过 Oster δ > 1 与高于最强控制变量的 E-value，标题主张就站得住。

**自检：** 如果 identification memo 写着 `causal_status: descriptive`，在动笔写正文之前先回到 §9.3 的“禁止主张”段读一遍 —— 你的语言上限从此被锁死。

## 9. `scholar-design` —— 数据之前先有设计

**目标：** 锁住估计对象、模型阶梯、样本限制、禁止语言。本节后，分析脚本基本是模板填空。

### 9.1 运行

```
> /scholar-design for RQ1, Social Forces, CFPS 2010-2020,
                 descriptive/decomposition design
```

### 9.2 `design/` 内容

```
design/
├── coef-map.csv
├── data-blueprint-...md
├── design-blueprint-...md
├── limitations-accepted.md
├── model-specs.json
├── pre-mortem-demographics-...md
├── pre-mortem-quant-...md
├── pre-mortem-senior-...md
├── project-brief.md
├── results-lock-...md
├── test-inventory.json
└── variable-dictionary.csv
```

### 9.3 估计对象与模型阶梯（真实蓝图节选）

```markdown
## 0. Headline finding（Phase 3.5 锁定）

本设计承诺以 Y2（用户每周互联网使用小时）为旗舰表与摘要句的焦点结果。

> 控制教育、收入、职业、家户构成、省 × 波次固定效应后，2010–2020 年
> CFPS 中国成人样本里，农业户口对每周互联网使用小时的惩罚在 2020 年
> 不小于 2010 年，尽管接入差距已从约 40 个百分点缩小到约 15 个 […]

## 1.1 假设 ↔ 估计量

| H  | 估计量                            | 识别假设                           |
|----|-----------------------------------|------------------------------------|
| H1 | Logit (Y1) + 省×波次 FE 的 OLS    | 在省×波次格内，户口与未观测基础  |
|    | （Y2|Y1=1，焦点）；Tobit MLE       | 设施的条件独立（Tobit 交叉验证另含|
|    | 交叉验证放在稳健性章节            | 删失 + 尾部分布假设）            |
|    | province × wave FE                | 设施条件独立                       |
| H2 | 个人 FE within-changes；         | HAPC：在年龄给定下，世代与时期   |
|    | HAPC；Deaton-Paxson bounds        | 可交换                             |
| H3 | 三向交互；Threefold Oaxaca-Blinder | 跨组共同支撑；组内线性          |
| H4 | 共住改变者上的 Person FE          | 不存在第三个未观测时变干扰        |

## 1.3 明确不主张
- 不对户口做因果解释
- 不对世代做因果解释（APC 不可识别）
- 本论文不做第三层（回报）主张
```

### 9.4 设计 pre-mortem 评审组

`scholar-design` 在**任何数据被读取之前**派出一个 **peer-reviewer 面板**——具体 agent 组合取决于设计类型。本例这个带 K≥3（户口×性别×队列）异质性族的定量设计派了三个：

- `peer-reviewer-quant` —— 定量方法评审
- `peer-reviewer-demographics` —— 测量与代表性评审（因设计带 K≥3 假设族而加入）
- `peer-reviewer-senior` —— 编辑匹配评审

面板**必派**，但裁决是**建议性**的：它写一份红黄绿备忘，你逐条接受或修改 RED 维度（最多 3 轮），`design-review-check.sh` 会因任何未接受的 RED 而拦住 Phase 4。

我们这次实际运行中，senior 评审一句关键话：*“Y1（接入二值）不该是 headline；Y2（使用强度）才是该论文真正的理论贡献，应该作为摘要句的焦点。”* 这一条让我们在跑任何分析之前就改掉了焦点结果，省掉一整轮修改。

**自检：** 打开 `limitations-accepted.md` 与 `model-specs.json`，能说出焦点结果、焦点表、焦点样本吗？说不出就别往下走。

## 10. `scholar-eda` —— 上模型之前先看清楚

**目标：** 建分析样本，诊断缺失，做 Table 1，检查分布——**在跑任何模型之前**。

### 10.1 运行

```
> /scholar-eda data/processed/cfps-panel-long.rds
              outcomes=y1_access,y2_hours,y3_breadth
              focal=hukou_rural,cohort,female,eduy
```

它写出 `scripts/01-build-sample.R`、`scripts/02-eda.R`，跑出：

- `tables/table1-descriptives.csv`
- `tables/missing-by-wave.csv`
- `eda/distributions/*.pdf`
- `logs/02-eda-<timestamp>.log`

### 10.2 真实 Table 1（节选）

| 分层 | n | 平均年龄 | 女性 | 农业户口 | 教育年 | y1_access | y2_hours均值 |
|---|---|---|---|---|---|---|---|
| **总体** | 204,418 | 44.6 | 0.497 | 0.749 | 7.54 | 0.329 | 12.07 |
| Wave 2010 | 33,595 | 42.4 | 0.493 | 0.844 | NA | 0.243 | NA |
| Wave 2012 | 35,716 | 42.2 | 0.505 | 0.698 | 7.28 | NA | NA |
| Wave 2014 | 37,140 | 43.2 | 0.494 | 0.709 | 8.03 | 0.369 | 11.58 |
| Wave 2016 | 36,833 | 50.2 | 0.496 | NA | 7.23 | 0.376 | 12.60 |
| Wave 2018 | 34,734 | 45.1 | 0.497 | 0.705 | 8.57 | 0.576 | 14.41 |
| Wave 2020 | 26,400 | 46.9 | 0.503 | 0.822 | 8.40 | 0.652 | NA |
| 户口：农业 | 119,259 | 42.8 | 0.501 | 1 | 6.49 | 0.243 | 11.45 |
| 户口：非农 | 35,762 | 42.6 | 0.488 | 0 | 10.33 | 0.492 | 12.51 |

### 10.3 像审稿人一样读这张表

- **Y1 在 2012 缺失，Y2 在 2010、2012、2020 缺失**——这是**测量窗口**问题。如果忽略它，“2010–2020 趋势”主张就是过度主张。验证阶段会抓到——但你现在注意到能省两天。
- **农业户口比例从 0.84 → 0.70 → 0.82 波动**——这是抽样框变化，需要 wave FE，蓝图已经预先指定。
- **教育年均值 7.28 → 8.57 上升** —— 世代替代信号，与 H2 一致。

**自检：** 用两句话写下你的 Y2 分析实际能用的波段（答案：2014–2018，这是工作坊的核心教训）。

## 11. `scholar-analyze` —— 出 headline 表

**目标：** 跑完整模型阶梯、保存表与图、写 results lock 让后续技能不能漂移。

### 11.1 运行

```
> /scholar-analyze data=data/processed/cfps-panel-long.rds
                  outcome=y2_hours
                  predictors=hukou_rural,cohort,female,eduy,
                              household_size,coresident_yng_adult
                  fe=province_x_wave
                  models=M1,M2,M3,M4,M5
                  journal=Social Forces
```

### 11.2 产出

```
scripts/
├── 01-build-sample.R        # 第 5A 阶段：harmonized 面板
├── 02-eda.R                 # 第 5A：Table 1 + 缺失
├── 03-models-Y1.R           # 第 5B：接入 logit 阶梯
├── 04-models-Y2.R           # 第 5B：使用强度线性 / Tobit 阶梯
├── 05-decomposition.R       # 第 5B：Oaxaca-Blinder, intersection cells
├── 05b-h3-corrected.R       # 第 7b：修正 H3 行
├── 06-figures.R             # 第 5B：六张图
├── render-pub-tables.py     # 第 5C：发表级表格
└── viz_setting.R            # ggplot 主题

tables/
├── table-Y1-models.csv / .html / .tex / -pub.md
├── table-Y2-models.csv / .html / .tex / -pub.md
├── table1-descriptives.csv
├── oaxaca-decomp.csv
├── intersection-cells.csv
├── results-registry.csv
├── spec-registry-Y1.csv / -Y2.csv
└── adjudication-log.csv     # H1/H2/H3/H4 判决与 p

figures/
├── fig1-access-trend.pdf
├── fig2-Y2-by-cohort.pdf
├── fig3-hukou-coef-trajectory.pdf
├── fig4-Y2-by-hukou-cohort.pdf
├── fig5-oaxaca-decomp.pdf
└── fig6-intersection-cells.pdf
```

### 11.3 真实 headline 结果（Y1 接入阶梯）

来自 `tables/table-Y1-models-pub.md`：

| 项 | M1 | M2 | M3（焦点） | M4 | M5（2014–2020） |
|---|---|---|---|---|---|
| 农业户口（vs. 非农） | -1.708\*\*\* | -0.910\*\*\* | -0.845\*\*\* | -0.724\*\*\* | -0.845\*\*\* |
|  | (0.036) | (0.048) | (0.051) | (0.077) | (0.051) |
| Cohort: 1996+ | -0.287 | -0.985\*\* | -0.891\*\* | -0.852\*\* | -0.891\*\* |
| 女性 | -0.410\*\*\* | -0.183\*\*\* | -0.212\*\*\* | -0.211\*\*\* | -0.212\*\*\* |
| eduy | — | 0.278\*\*\* | 0.269\*\*\* | 0.270\*\*\* | 0.269\*\*\* |
| household_size | — | — | -0.094\*\*\* | -0.093\*\*\* | -0.094\*\*\* |
| Num.Obs. | 148,599 | 108,526 | 108,509 | 108,509 | 108,509 |
| FE: province × wave |  |  | X | X | X |

*括号内 cluster-robust SE，按 `pid`。\* p<0.05, \*\* p<0.01, \*\*\* p<0.001。*

Y2（使用强度）表才是第二层故事的核心。锁定的 Y2 M3 焦点结果：

> 控制教育、收入、家户构成、省×波 FE 后，农业户口与用户每周互联网使用
> 时间相关 **−1.306 小时**（SE 0.295；BH-FDR p = 1.4e-5）。

Oaxaca 分解（`tables/oaxaca-decomp.csv`）显示**系数**部分（1.151 小时）主导**禀赋**部分（−0.395），支持制度排序解释，不支持纯资源解释。

### 11.4 但是“有结果”≠“结果有效”

**这正是工作坊的现实教训。** 当看到漂亮数字时**先别信**，先跑 §13（`scholar-code-review`）和 §15（`scholar-verify`）。

**自检：** 打开 `tables/results-registry.csv`，能从 headline 数字 `−1.306` 追到（a）产出脚本、（b）表格行、（c）样本量吗？少一环就不能用。

## 12. 像审稿人一样读三张图

`scholar-analyze` 跑出 6 张图。三张承担核心叙事。把它们当审稿人读。

### 12.1 Fig 1 —— 接入趋同

`figures/fig1-access-trend.pdf`：CFPS 成人按户口分组的互联网使用率随波次变化。

- **看到了什么：** 农业从 2014 ~21% 升到 2020 ~52%；非农从 ~48% 升到 ~71%；差距从 ~27 pp 缩到 ~19 pp。
- **手稿最初错写：** “差距从 2010 年的 40 pp 缩到 2020 年的 15 pp，跨 6 个波。”
- **验证捕捉到（CRIT-1）：** Y1 接入只在 2014、2016、2018、2020 测量——**4 波，不是 6 波**。“40pp / 15pp / 6 波”是图与数据的漂移。

substantive 论点（第一层趋同）保持，数字改成“27 pp → 19 pp，4 波 2014–2020”。§15 会展示这次修复怎么传播。

### 12.2 Fig 2 —— 世代分层

`figures/fig2-Y2-by-cohort.pdf`：用户每周使用小时按出生世代 × 波次。

- **看到：** 1985 后世代 ~14–16 小时/周；1965 前 ~6–9 小时/周。世代差大且基本跨波次稳定。
- **对 H2 的含义：** 与世代即原因一致；FE 规范下个人内年龄斜率近乎平坦——总体均值上升靠世代替代。
- **不能主张：** 世代“导致”——APC 不可识别，HAPC 与 Deaton–Paxson 仅作 bounds。

### 12.3 Fig 5 —— Oaxaca 分解

`figures/fig5-oaxaca-decomp.pdf`：城乡 Y2 差距的三分解堆叠柱。

- 总差距：**0.815 小时/周**
- 禀赋：**−0.395**（农业有些指标更“高”）
- 系数：**+1.151**（农业相同输入回报更低）
- 交互：很小

**系数（回报）部分主导**——制度排序预测的图样，纯资源解释预测不了。这张图承担论文的理论举证。

## 13. `scholar-code-review` —— 六个评审，一份报告

**目标：** 在相信任何数字之前，派出六个专门评审智能体审脚本。

### 13.1 运行

```
> /scholar-code-review scripts/
                       tables=tables/table-Y1-models.csv,
                              tables/table-Y2-models.csv,
                              tables/oaxaca-decomp.csv
                       figures=figures/fig1-access-trend.pdf,
                               figures/fig2-Y2-by-cohort.pdf
```

### 13.2 六个并行评审

1. `review-code-correctness` —— 逻辑错误、off-by-one、错引变量
2. `review-code-data-handling` —— 重新编码与代码本对照、缺失代码、样本限制
3. `review-code-statistics` —— 估计量与设计契合、SE、FDR
4. `review-code-reproducibility` —— 路径、种子、依赖、可端到端运行
5. `review-code-robustness` —— 边界、NA、静默失败
6. `review-code-style` —— DRY、命名、AI 痕迹

### 13.3 真实合并 scorecard

来自 `reports/code-review-2026-05-04.md`：

| 评审 | CRITICAL | ERROR | WARN | INFO | 判决 |
|---|---|---|---|---|---|
| review-code-correctness | 0 | 0 | 1 | 1 | PASS |
| review-code-data-handling | 0 | 2 (accepted) | 2 | 0 | PASS-w/-accept |
| review-code-statistics | 0 | 1 (accepted) | 2 | 1 | PASS-w/-accept |
| review-code-reproducibility | 0 | 0 | 2 | 1 | PASS |
| review-code-robustness | 0 | 0 | 2 | 1 | PASS |
| review-code-style | 0 | 0 | 0 | 3 | PASS |
| **合计** | **0** | **3 (accepted)** | **9** | **7** | **PASS** |

无 CRITICAL，但 **正确指出 H3 三向交互的 p 值取错了行**。同样问题在 §15 还会出现一次——这次智能体捕捉到大约 $0.30；如果由真审稿人在投稿后捕捉到，代价是 desk reject。

**自检：** 打开 `reports/code-review-statistics-...iter1.md`，找一条 WARN，决定（a）现在修，（b）写进 `analysis/limitations-accepted.md`，还是（c）降到讨论。

## 14. `scholar-write` —— 从锁定结果起草，不是凭空编

**目标：** 起草手稿，**每个数字**都能追到锁定 CSV，**每个引用**都打上待验证标记，**每个图引用**都对得上真图。

### 14.1 运行

```
> /scholar-write draft section=full-paper
                 results-lock=design/results-lock-2026-05-04.md
                 blueprint=drafts/section-blueprint.json
                 journal=Social Forces
                 word-target=10000
```

`scholar-write` 的读取顺序：results-lock → 章节蓝图 → 期刊 profile → 范文 → 禁止模式表 → 才开始起草。

### 14.2 真实摘要（来自 `drafts/manuscript-final-...md`）

```
Internet access in China rose from a minority privilege to a near-universal
condition between 2010 and 2020. […] Drawing on six waves of the China
Family Panel Studies (N = 204,418 person-waves; 54,825 unique respondents),
[…] agricultural-hukou status is associated with -1.306 weekly hours of
internet use among users (SE 0.295; BH-FDR p = 1.39e-5) in the focal
weekly-internet-hours model and with log-odds of access lower by -0.845
(BH-FDR p < 1e-60). The threefold decomposition of the rural-urban use gap
(total = 0.815 hours/week) attributes 1.151 hours to coefficient
differences and -0.395 hours to endowments, indicating that the gap
reflects differential returns to identical resources rather than shortfalls
in resources themselves. […]
```

注意正文里嵌入的**锚点**（HTML 注释）：

```
agricultural-hukou status is associated with -1.306 weekly hours
<!--anchor: lit focal-Y2-M3-->
... total = 0.815 <!--anchor: design total-gap-r4b--> hours/week ...
```

这些锚点是 `scholar-verify` 后续验证每个数字与锁定单元格匹配的依据。**不要删。**

### 14.3 自检

打开 `drafts/draft-manuscript-...md`，挑一句带数字的句子。验证：

1. 旁边有 `<!--anchor: ...-->`。
2. 锚点对应的单元格确实存在于 `tables/`。
3. 正文数字与单元格按显示精度一致。

三条任一不满足，就还不能进入验证阶段。

## 15. `scholar-verify` —— 工作坊核心一课

**目标：** 找出**你**在投稿前会漏掉的错误。

一条从不失败验证的流水线，是没认真检查的流水线。我们这次跑出 **7 个 CRITICAL** 与 **6 个 WARN**。这是**成功的**验证，不是丢脸的验证。

### 15.1 运行

```
> /scholar-verify manuscript.md results/ figures/
```

四个 agent 并行：

- `verify-numerics` —— 每条数字主张 → 锁定 CSV 单元格
- `verify-figures` —— 每处图引用 → 真实渲染文件（带视觉读图）
- `verify-logic` —— 每处方向 / 显著性主张 → 表格正确行
- `verify-completeness` —— 每个声明对象存在、被编号、被引用

### 15.2 七个 CRIT（真实）

来自 `verify/verification-report-2026-05-04.md`：

```
| Agent              | Verdict                              |
|--------------------|--------------------------------------|
| verify-numerics    | NEEDS-REVISION (1 WARN)              |
| verify-figures     | NEEDS-REVISION (4 CRIT, 2 WARN)      |
| verify-logic       | NEEDS-REVISION (2 CRIT, 3 WARN)      |
| verify-completeness| NEEDS-REVISION (1 CRIT, 5 WARN)      |
```

七个 CRIT（改写）：

1. **CRIT-1（Fig 1）。** 手稿写“6 波，40pp → 15pp”；数据是“4 波，27pp → 19pp”。**修：** 改正文。
2. **CRIT-2（Fig 2 副标）。** 副标 "2014–2020“；分析窗口 ”2014–2018“。**修：** 副标改 ”2014–2018"。
3. **CRIT-3（Fig 3 类型）。** 手稿描述“波次系数轨迹”；渲染是“Y1 描述柱图”。**修：** 正文改写为描述真实图形；系数轨迹改引表 2、表 3。
4. **CRIT-4（Fig 4 cohort × hukou）。** 三个主张与图不匹配。**修：** 重写。
5. **CRIT-5（Table 1 双身份）。** 表 1 既被引为“描述”又被引为“Y1 阶梯”。**修：** 重新编号。
6. **CRIT-6（H3 取错行）。** 摘要/结果/讨论/结论引用的 p = 0.92 是主效应行，不是三向交互行。**修：** 从 `adjudication-log.csv` 的 H3-CORRECTED 重抽（结论"H3 NOT supported"不变）。
7. **CRIT-7（Y1 M3 N）。** 同时报 108,526 与 108,509 两个 N。**修：** 锁定为 108,526。

### 15.3 流水线影响

按项目的 `feedback_preserve_ai_failure_cases` 规则，**不**整稿重写，而是**逐处定点**修复后重跑验证：

```
CRITs addressed:
- CRIT-1: 摘要/方法/结果改为 "four waves (2014–2020), 27 pp → 19 pp"。
- CRIT-2: 加澄清句；图副标更新延后到 R&R。
- CRIT-3: 结果叙述改为 M1 接入差距 pp 轨迹；系数轨迹引用改路由到表。
- CRIT-4: 三句被改写为与渲染图相符的描述。
- CRIT-5: 表 1=描述，表 2=Y1 阶梯，表 3=Y2 阶梯，表 4=Oaxaca，表 5=交叉。
- CRIT-6: H3 p 从 H3-CORRECTED 行重抽；H3 NOT supported 结论保留。
- CRIT-7: 统一为 N = 108,526。
```

headline 发现（Y1 趋同 + Y2 持续 + Oaxaca 系数主导）**所有 CRIT 都没动到**。修正反而把手稿打磨得更稳——**这就是验证的意义。**

**自检：** 从你的稿子里挑一句话，按“正文 → 表 → 脚本 → 样本 → 日志”追一遍。任意一环缺，这句话就不能投。

## 16. `scholar-citation` —— 引用不能凭氛围

**目标：** 验证每条参考文献，替换掉编造的，导出干净的 BibTeX。

LLM 会幻觉引用：作者名、卷期、DOI 都“看起来真”。这个技能就是为它存在。

### 16.1 运行

```
> /scholar-citation verify manuscript.md
> /scholar-citation manuscript.md ASA export
```

执行内容：

- 本地参考库（Zotero / Mendeley / BibTeX）
- CrossRef DOI 验证
- 网络检索本地未命中的项
- Retraction Watch 撤稿数据库
- 不能确认的项替换成 `[CITATION NEEDED — verify]`

### 16.2 这条规则的现实意义

2026 年 4 月对 26 篇 AI 生成社会科学论文的审计中，**得分最高的论文也被审稿人标出一条可疑的 2023 年后引用**。我们这次数字鸿沟运行里，验证发现的未确认引用中，CrossRef 检验后**有两条是编造的**：一篇并不存在的 2024 论文；一个 2023 年 DOI 指向的是无关文章。两者都已从手稿中移除。

把这条规则贴到电脑上：**No citation by vibe.** 每条引用必须验证、标记或删除。

## 17. `scholar-polish` —— 最后做，不是先做

**目标：** 改善文字流动、语域、作者声音；**不**改主张、发现、因果强度。

```
> /scholar-polish scan manuscript.md
> /scholar-polish rewrite manuscript.md  # 仅在 verify PASS 之后
```

模式：

- **scan** —— 诊断 AI 通用文风（套语、对仗式 hedging、方法清单泄漏、伪引用密度），但不写。
- **rewrite** —— 应用定点编辑。

Polish **永远不能**：

- 改数字
- 加强因果主张
- 增加引用
- 删掉限制

接受改动前**先 diff**：

```bash
$ diff drafts/draft-manuscript-...md drafts/draft-manuscript-polished-...md \
    | head -50
```

如果 diff 把 "X is associated with Y“ 改成 ”X causes Y"，**拒绝这次 polish**，缩小作用域。

## 18. `scholar-respond` + `scholar-journal` —— 投稿前

**目标：** 模拟审稿，检查期刊匹配，准备 cover letter 与投稿包。

```
> /scholar-respond simulate
                   manuscript=drafts/manuscript-final-...md
                   journal=Social Forces
> /scholar-journal Social Forces drafts/manuscript-final-...md
```

`scholar-respond simulate` 派出 3–4 个针对目标期刊校准的评审 agent：

- `peer-reviewer-quant` —— 方法严谨度
- `peer-reviewer-theory` —— 概念贡献
- `peer-reviewer-demographics` —— 代表性、分解
- `peer-reviewer-senior` —— 编辑匹配、R&R 建议

产出严重性矩阵与修订路线。**模拟审稿不能替代真实评审**——它的作用是让你带着更好的问题去问真人。

`scholar-journal` 检查：字数 vs. 上限、摘要结构、IRB / 伦理声明、数据可得性声明、双盲合规、格式、cover letter 草稿。

## 19. `scholar-replication` + `scholar-open` —— 可复现是习惯，不是临投稿

```
> /scholar-replication build output/digital-divide-china-cfps
> /scholar-open prepare output/digital-divide-china-cfps
```

复制包包含：

- 按执行顺序的脚本，配一个主编排脚本 `run-all.sh`（驱动 R 控制器 `00_master.R`）
- `environment.yml` / `renv.lock` 锁文件
- 按 AEA 模板的 README
- `data-availability.md`：什么共享、什么不共享（CFPS 原始数据受限；分享派生表、代码、模拟数据、访问说明）
- 锁定表的预期输出哈希（SHA256），任何人重跑都可比对

如果等到投稿周才做，可复现性就成了考古学。

## 20. `scholar-presentation` 与 `scholar-grant` —— 下游产物

**会议报告 / job talk：**

```
> /scholar-presentation talk output/digital-divide-china-cfps
                         manuscript.md figures/
                         target=ASA 15min
```

输出：`slides.pptx`、`slides.pdf`、演讲稿、备份页、时间提示、简化图。

**盒装风格 PPTX 布局**（按用户偏好）：用带边框的盒子包内容块，而不是横线分隔——投影时更清晰。

**Pilot → 经费：**

```
> /scholar-grant NSF sociology concept-note
                 digital divide aging China
                 using CFPS pilot findings
```

输出：aims、significance、broader impacts、数据管理计划、预算说明草、模拟评审。

通用规则：每条下游产物都要追回锁定结果、已验证引用，或被接受的限制。**演示是在时间压力下选择主张，不是装饰。**

# 第三部分：编排器

到此为止我们一次跑一个技能。要写一篇真正的论文，需要一个可恢复、有关卡的整链工作流——这就是 `scholar-full-paper` 与 `scholar-auto-research`。

## 21. `scholar-full-paper` —— 当前权威重链

```
> /scholar-full-paper --slug digital-divide-china-cfps
  "RQ: In CFPS 2010-2020, did hukou/cohort gaps in internet access narrow
   while gaps in weekly use hours persisted? Target Social Forces."
```

active 线性路由（由 `scripts/gates/pipeline-state.sh` 定义）：

| 阶段 | 内容 | 关卡 |
|---|---|---|
| **−1** | 安全扫描 | 全部 CLEARED / LOCAL_MODE |
| **0-PRE** | （可选）头脑风暴 | Top-5 RQ |
| **0** | Idea selection | 一个焦点 RQ |
| **1** | 研究简报 | project brief |
| **2** | 文献 + 理论 | 假设导出 |
| **3** | 设计蓝图 | 估计量 + 模型阶梯 |
| **3.5** | 设计 pre-mortem | 三个评审 PASS |
| **4** | 数据蓝图 | 变量字典冻结 |
| **5** | EDA + 分析计划 | Table 1 + 缺失图 |
| **5A.5** | 执行前代码评审 | 脚本评审过 |
| **5A.7** | 分析 pre-mortem | 评审组同意 |
| **5B** | 执行分析（Phase 5 内部，无单独 state gate） | 表 + 图渲染 |
| **5.5** | 完整代码评审 | 6 评审 PASS |
| **5C** | Runtime sanity | 数字可重现 |
| **6** | 计算 / 语言学分支（条件） | 分支专属产物 |
| **6.2** | 计算 pre-mortem（仅当 Phase 6 启用） | 评审组通过计算计划 |
| **6.5** | Results lock + pre-draft 验证 | SHA256 manifest |
| **6.8** | Section blueprint | 章节级写作契约 |
| **7** | 手稿起草 | 按 blueprint 完整起草 |
| **7b** | 验证关卡 | 4 评审 PASS |
| **7c** | 风格润色 | diff 审过 |
| **7c.5** | 文稿质量复查 | Codex 跨模型文稿面板 + Claude 整体评审 PASS |
| **8** | 引用合规 | 全部验证 |
| **9** | 投稿包 | cover letter + 期刊格式投稿 |
| **9b** | 伦理合规 | IRB / AI 披露 |
| **10** | Pre-submission 模拟评审 | R&R 严重性矩阵（建议） |
| **10.5** | 手稿质量关（双 pass） | Phase 11 之前的硬关卡 |
| **11** | 最终发表级组装 | docx/pdf/tex 归档 |
| **11b** | 投稿准备 — reviewer 交接 | reviewer-facing 手稿 |
| **11.5** | 投稿卫生 | 无路径泄漏，无流程术语 |
| **12** | 复制包（v5.13 起从 9c 重新编号） | 预飞行检查 + build/document/test/verify；SHA256 lockfile |

强制 "do not skip" 关卡：**Phase 3.5、5A.5、5A.7、5.5、5C、6.2（计算分支启用时）、6.5、7b、7c.5、9b、10、10.5、11.5、12**。Phase 7 起草必须在 `results-locked/LATEST.txt` 存在且 `results-lock-verify.sh` 退出 0 之后才能开始。

这些关卡无法强行绕过。自 **Layer-3 硬阻断**（2026-05-18）起，试图在 RED 关卡上强制完成（`SCHOLAR_PSTATE_FORCE_REASON`，即 "HB3"）或把流水线上限设到 RED phase 之后（`set-authorized-through`，即 "HB1"），都会在调用点被拒绝、记入 `logs/hardblock-refusal-audit.md`，并标记为 `phases_force_complete_blocked`。越过 RED 关卡唯一诚实的路径是修复缺陷或 `pipeline-state.sh halt <phase>`。哪条规则管哪个此类决策，写在内联进你 `CLAUDE.md` 的**决策触发记忆映射（decision-trigger memory map）**里。

**随时恢复：**

```
> /scholar-full-paper resume digital-divide-china-cfps
```

读取 `output/<slug>/logs/project-state.md`（state 块的规范路径，见 `scripts/gates/pipeline-state.sh`），识别上次完成阶段并继续。Phase 7b 验证发现严重问题时，编排器**回退**到 Phase 5 或 7，不是往前打补丁。

### 21.1 26 篇审计的实证基线

> **来源与注意事项。** 下方数字来自 `workshop/workshop-papers-analysis-2026-05-07.md`（1,369 行审计备忘，2026-05-07 生成）。方法：从 `workshop/cfps-example/output/` 与 `workshop/GSS/Projects/output/` 抽取的 26 篇 AI 生成稿件，由 5 个并行的领域评审 agent 用统一评分表（理论 · 数据 · 方法 · 发现 · 3-审稿模拟 · 期刊判定）以 Zhang 2017 *JMF* 为基准 1–10 打分；成本估算依据稿件字数 + 工件大小 + 脚本数（无 API 直接日志）。评分表为内部口径，未经正式验证 —— 外部引用前请用你自己的审计替换。

来自审计（按 §Re-analysis 修正后的分单元统计）：

| 配置 | 平均分 (满分 10) | N | 来源 |
|---|---|---|---|
| `scholar-full-paper` × Claude Code | **6.36** | 18 | 审计 §Re-analysis 第 1094 行 |
| `scholar-auto-research` × Claude Code | 5.50 | 3 | 审计 §Re-analysis 第 1094 行 |
| `scholar-auto-research` × Codex CLI | 4.40 | 5 | 审计 §Re-analysis 第 1095 行 |
| `scholar-full-paper` × Codex CLI | （空格 —— 建议跑 3–5 篇填上） | 0 | — |
| **全集平均** | **5.94** | 26 | 审计 §Headline 第 60 行 |

成本（按审计 per-paper 列）：约 **$20–$60/篇**，26 篇合计约 **$700–$1,200**（差异由稿件字数决定：3,000 字稿约 $20，14,000 字稿约 $60）。

多数产出是**可修草稿**而不是 submission-ready（中位判定：Q2 期刊 Major Revision）。结论：`scholar-full-paper` + Claude Code + 人工验证关卡是当前最佳格（均值 6.36，n=18）；`Codex × scholar-auto-research` 格最弱（均值 4.40，n=5），编排器或可在 v5.18.0 / v5.19.0 关卡升级后改善（尤其在 Claude 上）—— 重跑后再评估。

## 22. `scholar-auto-research` —— 教学用确定性脚手架

```
> /scholar-auto-research --slug demo-project "<研究想法>"
> /scholar-auto-research resume output/demo-project
```

它用 `references/phase-contract.json` 写死 21 个阶段（0–20）。每个阶段都有 `required_inputs`、`required_outputs`、`verifier`（返回 0 表示 PASS 的 shell 命令）、`next_phase`、`route_back_phase`。

权威 phase 列表（来自 `phase-contract.json`，是单一事实来源）：

| # | 阶段 | 必需产物 |
|---|---|---|
| 0 | Safety | `safety-status.json`；高风险未解决文件阻塞流程 |
| 1 | Research Question | 候选 RQ、期刊匹配、选定 RQ JSON、选择理由 |
| 2 | Literature and Theory | `lit-theory.md`、覆盖度矩阵、已验证 `references.bib` |
| 3 | Design | 设计蓝图、模型设定、识别策略、修订日志 |
| 4 | Data and Measurement | 变量字典、数据状态、测量计划、数据 manifest |
| 5 | Analysis Plan | spec registry、计划脚本清单、分析计划（无执行） |
| 6 | Pre-Execution Review | 六维度计划代码评审 + 修复日志 + 复审 |
| 7 | Analysis Premortem | premortem 风险登记、null-falsification 表、决策规则 |
| 8 | Execute Analysis | 执行报告、results registry、figure registry |
| 9 | Post-Execution Review | 执行后评审 + 修复日志；未解决阻塞回到 6 |
| 10 | Runtime Sanity | runtime sanity 报告（可重现性、不变量、漂移检查） |
| 11 | Results Lock | 不可变结果快照、manifest hash、Stage 1 verify |
| 12 | Manuscript Blueprint | 章节级写作契约 |
| 13 | Draft Manuscript | 按 blueprint 完整起草 |
| 14 | Verify Manuscript | 验证报告（数字、图、逻辑、完整性） |
| 15 | Citation and Claim Support | 引用审计 + claim-source 映射 |
| 16 | Ethics and Open Science | 伦理 + 开放科学声明 |
| 17 | Replication Package | 复制包（脚本、数据说明、环境） |
| 18 | Manuscript Quality Gate | 质量关报告；Phase 19 之前的硬关 |
| 19 | Final Assembly | 最终 md/docx/tex/pdf |
| 20 | Submission Hygiene | 投稿洁净输出（无路径泄漏、无流程术语） |

默认路由止于 **Phase 20**。可选下游产物（grant、presentation、resubmission、auto-improve）不在范围内，作为独立技能调用。

适合**课堂演示与流程原型**，不适合严肃论文（用 full-paper）。

如果你想搭自己的编排器，复制这个结构：`phase-id` → `purpose` → `required inputs` → `actions` → `outputs` → `verification gate` → `next/route-back`。先为自己的流程写五个阶段，再尝试整链。

## 23. Codex 作为外部审查者

**目标：** 独立性。跑流程的智能体不是评判流程的可靠人选。

Claude 跑完后交给 Codex：

```bash
$ cd output/digital-divide-china-cfps
$ codex
```

```
> Audit scripts/04-models-Y2.R against design/design-blueprint-...md.
  Check that: (a) 焦点 Y2 估计量为 Y1=1 条件下的 OLS + province × wave FE，并用 Tobit MLE 作为交叉验证（依据 CRIT-STAT-001）；
  (b) cluster-robust SE 按 `pid` 聚类；(c) 在 H1–H4 焦点检验上应用 BH-FDR；
  (d) 最终系数与 tables/table-Y2-models.csv M3.hukou_rural 在 3 位小数下一致。
  逐条返回 PASS / FAIL / UNCERTAIN，附一句证据。
```

Codex 会读脚本、蓝图、表，给出四行 PASS/\allowbreak{}FAIL/\allowbreak{}UNCERTAIN——这就是代码评审格式，区别在评审人是**另一家厂商的模型**，这正是关键。

**不要**让 Codex：

- “把论文修了”（无约束 → 大改）
- “补缺失数据”（永远不该问）
- “选期刊”（编辑判断是你的）

# 第四部分：负责任的实践

## 24. 新项目的前 20 分钟

每开新项目：

1. **建目录：**

   ```bash
   mkdir -p projects/<slug>/{data/raw,data/interim,data/processed,\
                             materials,output,logs}
   ```

2. **把原始数据放进 `data/raw/`，不要手工修改。**
3. **`cd projects/<slug>` 然后 `claude`。**
4. **跑 `/scholar-init --slug <slug>`。**
5. **跑 `/scholar-init review`，** 解决每一个 NEEDS_REVIEW。（`review` 模式属于 `scholar-init`，不是 `scholar-safety`。）
6. **跑 `/init`** 生成 `CLAUDE.md`，编辑它，加上禁止动作。
7. **跑 `/scholar-brainstorm`** 拓宽菜单，人工选一个 RQ。
8. **跑 `/scholar-idea`，** 确认假设是预先指定的。

8 步全做完之前，不要让智能体跑模型。

## 25. 五个最常见的学员错误

1. **“帮我写一篇关于 X 的论文。”** —— 跳过第 7 步，让智能体自己捏造问题与证据。
2. **让 AI 读所有东西。** —— 跳过 `scholar-safety`；原始行进上下文，隐私边界丢了。
3. **凭感觉接受引用。** —— 跳过 `scholar-citation verify`；参考文献变科幻。
4. **忽略日志。** —— 验证发现问题时无审计轨迹。
5. **先润色再验证。** —— 把错误主张润得更自信。顺序反过来：先验证，最后润色。

## 26. 带走自查清单

逐条当作承诺：

- [ ] 在让智能体读取敏感数据前先跑 `scholar-init` + `scholar-safety`。
- [ ] 给每个项目写 `CLAUDE.md`。
- [ ] 任何高风险多步操作先切到 `plan` 模式（`Shift+Tab`）。
- [ ] 把 `output/<slug>/scripts/` 当作分析的唯一真理来源。
- [ ] 在起草前锁定结果（`scholar-analyze` → `results-lock-*.md`）。
- [ ] 在相信稿中任何数字前跑 `scholar-verify`。
- [ ] 投稿前跑 `scholar-citation verify`。
- [ ] 仅在验证 PASS 后跑 `scholar-polish`。
- [ ] 高风险主张用第二厂商智能体（Codex）做外部审查。
- [ ] 在验证日志里**保留** AI 失败案例，不要静默重写。

## 27. 五条负责任原则

1. **披露。** 哪些 AI 工具、在哪些阶段、做了什么角色，要写清楚。（`scholar-ethics` 会替你生成披露文本。）
2. **验证。** 每条主张 → 表 → 脚本 → 样本。数字、引用、图、假设——全都要。
3. **保持技能。** 不要把“你本应自己会做”的事完全外包；每年至少手算一次回归。
4. **保护原创。** 研究问题、理论判断、识别决断、最终责任——**不能**外包。
5. **关注公平。** AI 是已有制度差距的乘数。把脚本、代码本、模拟数据、技能慷慨分享出去。

## 27A. 与 Anthropic 4D 框架的对照

Anthropic 官方 AI Fluency 课程把所有人与 AI 的互动组织在四个动词之下 —— 即 **4D 框架**：**Delegation（委派）、Description（描述）、Discernment（辨识）、Diligence（尽责）**。本工作坊的五条原则、§3 的动手协议、以及每一个 scholar-skill，都可以识别为这四种动作之一的具体实例。这张对照表给学员一份与 Anthropic 自家训练对齐的词汇，工作坊结束后他们继续学习时能直接接上。

<div class="hb-table-wrap">
<table>
<thead><tr>
<th><strong>4D</strong></th><th><strong>Anthropic 怎么教</strong></th><th><strong>在本工作坊的对应位置</strong></th>
</tr>
</thead><tbody>
<tr>
<td><strong>Delegation<br> （委派）</strong></td><td>决定什么交给 agent、什么留给人；项目规划</td><td>§3.5 模型选择器（Haiku / Sonnet / Opus 分档）· V×A 委派类型学（输出可验证性 × 过程可表达性）· 收束块里的委派框架</td>
</tr>
<tr>
<td><strong>Description<br> （描述）</strong></td><td>有效提示 —— 输入契约</td><td>§5 提示词解剖 · §3.3 CLAUDE.md 作为稳态简报 · §8D <code>identification-memo.md</code> 作为结构化输入契约</td>
</tr>
<tr>
<td><strong>Discernment<br> （辨识）</strong></td><td>批判性评估；<em>Description ↔ Discernment 循环</em></td><td>§13 <code>scholar-code-review</code> · §15 <code>scholar-verify</code>（工作坊的核心一课）· §23 Codex 作为外部审查者</td>
</tr>
<tr>
<td><strong>Diligence<br> （尽责）</strong></td><td>验证 + 负责任使用；最后一道闸</td><td>§27 上面的五条原则 · §26 以 <em>Verify</em> 收束的可复用工作流 · §19 <code>scholar-replication</code> / <code>scholar-open</code></td>
</tr>
</tbody></table></div>

Anthropic 强调而你容易忽视的一点：**Description 与 Discernment 是一个循环**，不是两个独立步骤。这正是 §3 的请求 → 提议 → 批准 → 产物 → 验证循环在做的事 —— 每一次批准都是一次 discernment，它修改下一次 description。如果你的会话感觉是“一次性提示词 + agent 长独白”，那循环已经塌了，质量也会跟着塌。

## 28. 结束

当智能体能跑完整流程，什么变得更值钱？

> 你的问题。你的判断。你的责任。

本手册里的技能不是让 AI 听起来更学术，而是让 AI **留下可检查的学术产物**。可检查的产物——这是学术研究在每一次新工具引入（活字、统计软件、编码智能体）之后能够生存的方式。

现在，去一个真实项目目录里打开 `claude`，跑 `/scholar-init`。前 20 分钟，是你能做的最重要的投资。

\vfill

*CFPS 数字鸿沟示例的全部代码、脚本与产物：*
`Claude-Code-Skill/workshop/cfps-example/output/digital-divide-china-cfps/`

*Open Scholar Skills 仓库：* `github.com/joshzyj/open-scholar-skill`

*工作坊材料更新：* `ZhangYGroup/VibeRes4SS/`

# 第五部分：附录——完整的真实产物

本部分附录收录 2026 年 5 月 4–5 日 CFPS 数字鸿沟流程**原汁原味、未编辑**的全部报告。第二至四部分中所引用的片段都是从这里挑出来的。把它们当作“端到端智能体流程实际产出了什么”的法证证据——包括笔误、四舍五入警告、未完成项以及被记录在案的失败案例。

> 注：技能产物本身由智能体以英文生成（CFPS 变量名、文件路径、表头都使用英文）。本附录保留原文，方便学员直接对照磁盘上的实际文件。

## 附录 A —— `scholar-brainstorm` 执行摘要（完整）

*文件：`output/digital-divide-china-cfps/` `scholar-brainstorm-`
`digital-divide-china-cfps-top5-summary-2026-05-05.md`，2026-05-05 生成。*

###  Research Question Brainstorm - Executive Summary
#### Digital Divide in China Using CFPS Materials
*Generated by /scholar-brainstorm on 2026-05-05*
*Operating mode: MATERIALS*

---

#### Dataset Overview

The supplied materials are CFPS questionnaires and codebooks covering 2010-2020. CFPS is a nationally representative longitudinal survey of Chinese individuals, households, families, and communities, with rich modules on economic activity, education, family dynamics, migration, health, and internet use. This run did not include raw data files, so the ranking is based on measurement coverage, theory, and verified literature rather than empirical signal tests.

#### Top 5 RQs

####### #1: Access Convergence, Use Divergence

**RQ:** In China from 2010 to 2020, did the hukou, education, and cohort gaps in internet access narrow while gaps in productive use, use intensity, and use breadth persisted or widened?

**Variables:** `U201`, `U202`, `U250M`, `U701`-`U705`, hukou, education, cohort, gender, income, household composition.

**Why strongest:** Best flagship paper. It uses CFPS's panel structure to separate first-level access from second-level productive use and can speak directly to stratification theory.

**Method sketch:** Panel models, wave/province controls, individual fixed effects where feasible, and decomposition of rural-hukou or cohort gaps.

####### #2: Remote-Work Divide During COVID-19

**RQ:** Did mobile-only internet access, computer internet access, and job-level computer requirements determine who could shift to remote work during the 2020 COVID shock, and did this protect workers from income loss?

**Variables:** `U201`, `U202`, `U201A`, `U202A`, `G19`, `COVID5`, `COVID4`, `COVID601`, `COVID602`, `G11`, `G12`.

**Why strong:** Turns the digital divide into a shock-resilience question. The 2020 work module gives a clear pandemic hook.

**Method sketch:** Employed 2020 respondents, occupation/industry/province controls, and income-loss models by device access and digital job compatibility.

####### #3: Online-Learning Outcome Divide

**RQ:** During COVID-19 school closures, did rural/hukou and parental-education differences in device access and online-learning intensity translate into unequal study time, tutoring, education spending, and aspirations?

**Variables:** `COVID3`, `U94`, tutoring participation/time/spending, education spending, study time, aspirations, parental education/income, hukou.

**Why strong:** CFPS can connect student online learning to household resources and education spending, which many school-only surveys cannot.

**Method sketch:** Student/child subsample, decomposition of rural-urban or parental-education gaps, and pre-2020 baseline controls where mergeable.

####### #4: Older-Adult Digital Health and Social-Connection Divide

**RQ:** Among adults aged 60+, does internet use improve self-rated health, mental health, happiness, and social connectedness, and are returns concentrated among urban, educated, or co-resident-with-younger-family older adults?

**Variables:** Internet access/use, `U701`, `U703`, `U802`, `U11`, health and mental-health items, `M2016`, `M2011`, household composition.

**Why viable:** CFPS supports panel health analysis, but the area is crowded. It needs a sharper mechanism, especially household digital transmission or type-of-use heterogeneity.

**Method sketch:** 2014-2020 older-adult panel, fixed effects, lagged internet use where possible, and heterogeneity by hukou/education/living arrangement.

####### #5: Information Trust, Privacy Concern, and Platform Dependence

**RQ:** Does dependence on WeChat, short video, and online news create unequal information trust and privacy/data-governance attitudes across age, education, and hukou groups?

**Variables:** `U11`, `U111`, `U93`, `N202`, `U802`, `U13`, `U110`, `U121`-`U123`, `N1001`.

**Why distinctive:** Moves beyond access and use into platform-mediated trust, misinformation risk, and privacy attitudes. Main constraint: some 2020 items are restricted data.

**Method sketch:** 2020 cross-sectional models, age/education/hukou interactions, and latent-class typology of platform dependence and privacy/trust attitudes.

#### Recommendation

Pursue RQ1 as the main paper. It has the strongest combination of data readiness, theoretical breadth, and publication fit because it uses CFPS's central advantage: repeated individual-level observation during China's access-saturation transition. RQ2 is the best alternative if the desired paper should be more timely and shock-oriented; it converts digital inequality into a labor-market resilience question during COVID-19. RQ5 is the most novel side project but should only be pursued if the restricted 2020 privacy and information-trust items are accessible.

RQ3 is feasible and policy-relevant, but the COVID online-learning literature is already crowded; the contribution must be household linkage, not simply another rural-urban learning-gap paper. RQ4 is substantively important, but multiple recent CFPS studies already examine internet use and older-adult health, so novelty depends on reframing around intra-household digital support, type of online use, or heterogeneous returns.

Verified anchors used for this ranking include the [CFPS official introduction](https://www.isss.pku.edu.cn/cfps/en/about/introduction/index.htm), [ICPSR CFPS study page](https://www.icpsr.umich.edu/web/ICPSR/studies/36524), Ren and Zhu's 2024 [age-based digital divide study](https://www.sciencedirect.com/science/article/pii/S0308596124000132), Yu et al.'s 2026 [CFPS financial-vulnerability study](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0343501), and He et al.'s 2019 [WeChat rumor study](https://journals.sagepub.com/doi/10.1177/2158244019876273).

## 附录 B —— `scholar-brainstorm` 长报告（完整）

*文件：`output/digital-divide-china-cfps/` `scholar-brainstorm-`
`digital-divide-china-cfps-top5-2026-05-05.md`，2026-05-05 生成。包括运行模式、材料摘要、变量清单、主题聚类、候选 RQ、评分短列表、Top-5 完整细节、评估小组与引用验证。*

###  Scholar Brainstorm: Top 5 Research Questions on the Digital Divide in China
*Generated by /scholar-brainstorm on 2026-05-05*
*Operating mode: MATERIALS*

---

#### Operating Mode

Input path: `materials/`

Classification: MATERIALS mode. The directory contains CFPS questionnaires, technical reports, one cross-year codebook workbook, and one CFPS literature workbook. It does not contain raw analytic data files supplied for this invocation, so empirical signal tests were skipped.

Safety status: N/A - no raw data file was read into model context.

#### Material Summary

| Field | Value |
|---|---|
| Dataset family | China Family Panel Studies (CFPS) |
| Material type | Questionnaires plus codebook/literature workbook |
| Unit of analysis | Individual, household, family, and community |
| Temporal coverage in materials | 2010, 2012, 2014, 2016, 2018, 2020 |
| Design | Nationally representative longitudinal panel; CFPS is described by ISSS as a biennial longitudinal survey launched in 2010 |
| Sampling note | ICPSR describes 16,000 target households in 25 provincial-level regions, representing about 95% of China's population, with individual, household, and community units |
| Codebook note | `CFPS 2018 codebook.xlsx` is `CFPS2018crossyearid_202104`, N = 74,130, 95 cross-year variables |
| Key limitation | This run used questionnaires/codebooks only; ranking is theory and measurement based, not based on estimated effects |

Sources verified: [CFPS official introduction](https://www.isss.pku.edu.cn/cfps/en/about/introduction/index.htm), [ICPSR CFPS study page](https://www.icpsr.umich.edu/web/ICPSR/studies/36524).

#### Variable Inventory

####### Digital Access and Use

- Mobile phone use and costs: `U1`/`U1M`, `U102`, `U102A`.
- Mobile internet and computer internet: `U201`, `U202`; 2020 adds daily mobile and computer internet minutes, `U201A`, `U202A`.
- General internet frequency and breadth: `U701` learning, `U702` work, `U703` social, `U704` entertainment, `U705` commercial activity; 2018/2016 include `U250M` weekly leisure internet hours.
- Digital consumption and leisure: `U7051` online shopping expenditure, `U91` online games, `U92` online shopping, `U93` short video/live streaming, `U94` online learning.
- Platform and information items: `U11` WeChat use, `U111` WeChat Moments sharing, `U13` trust WeChat Moments vs official media when conflicting, `U802` internet as information channel, `N202` online political-news exposure.
- Privacy and data governance: `U110` privacy leakage concern, `U121` government personal-data collection acceptance, `U122` gene-company/law-enforcement data sharing, `U123` health-app data sharing. These 2020 items are marked in the questionnaire as general restricted data.
- Labor-market digitalization: `G19` computer required at work, `COVID5` remote work during Feb-Mar 2020, `G603` phone always-on requirement.
- Education digitalization: `COVID3` online learning time, school online-teaching adoption, online/offline tutoring indicators and spending.

####### Outcomes and Moderators

- Labor outcomes: employment, job class, work hours, work income `G11`/`G12`/generated `Income`, job security, insurance, workplace.
- Education outcomes: study time, tutoring participation/time/spending, education spending, aspirations, school type and education history.
- Health and well-being: self-rated health, mental health modules, sleep, health behavior, happiness `M2016`, social relations `M2011`.
- Social capital and trust: contact frequency with kin, online-to-offline tie formation `U601`-`U603`, generalized trust `N1001`, specific trust batteries.
- Stratifiers: hukou `HK10`-`HK18` and 2020 `A301`, rural/urban residence, birth cohort, gender, education, income, household composition, co-resident children/young adults, province and community context.

Star variables:

1. `U201` plus `U202` - separates mobile-only access from computer-enabled access.
2. `U701`-`U705` - separates productive use from leisure/social/commercial use.
3. `COVID5` - captures an exogenous pandemic-period need for remote work.
4. `COVID3` plus tutoring/spending items - captures school closure online-learning adaptation.
5. `U13`, `U110`-`U123` - unusually strong measures for information trust, privacy concern, and data-governance attitudes.
6. CFPS panel identifiers and cross-wave hukou/education/employment variables - allow longitudinal stratification designs.

#### Thematic Clusters

| Cluster | Core variables | Main role |
|---|---|---|
| Access ladder | `U201`, `U202`, `U201A`, `U202A` | X/Y |
| Productive use | `U701`, `U702`, `U705`, `U250M`, `G19` | X/M/Y |
| Digital leisure | `U91`, `U93`, `U704` | X/M |
| Online education | `COVID3`, `U94`, tutoring and education-spending items | X/Y/M |
| Digital labor market | `COVID5`, `G19`, `G11`, `G12`, `Income`, `G603` | X/Y |
| Social networks and trust | `U11`, `U111`, `U601`-`U603`, `N1001`, `M2011` | X/M/Y |
| Information governance | `U13`, `U110`-`U123`, `N202`, `U802` | X/Y |
| Stratification axes | hukou, rural/urban, cohort, gender, education, household composition | W/C |

#### Candidate Research Questions

| # | Candidate RQ | Strategy | Data readiness |
|---|---|---|---|
| 1 | As internet access expands, do hukou and cohort still stratify productive internet use and use intensity? | Temporal/change | High |
| 2 | Does mobile-only access versus computer access predict who could work remotely and avoid income loss during COVID-19? | Gap-driven | High |
| 3 | Did online learning during COVID-19 widen rural-urban and parental-education gaps in study time, tutoring, and educational aspirations? | Outcome-driven | High |
| 4 | Among older adults, does internet use improve health, happiness, and social connectedness, and for whom? | Mechanism | Medium-high |
| 5 | Does reliance on WeChat/short video/online news reshape information trust, privacy concern, and institutional trust differently by age, education, and hukou? | Gap-driven | Medium-high |
| 6 | Does commercial internet use and online shopping reduce household financial vulnerability or deepen consumption/credit risk? | Mechanism | Medium |
| 7 | Does social internet use substitute for or complement offline kin contact and friendship networks? | Mechanism | Medium |
| 8 | Does computer use at work generate wage returns independent of education and occupation? | X-first | Medium |
| 9 | Are women, rural residents, and older cohorts concentrated in low-return forms of digital use? | Heterogeneity | High |
| 10 | Does co-residence with digitally skilled children or young adults reduce older adults' digital exclusion? | Mechanism | Medium |
| 11 | Does internet use for political information alter generalized trust or local-government trust? | Gap-driven | Medium |
| 12 | Does online dating or online spouse meeting change assortative mating patterns? | X-first | Medium |
| 13 | Is mobile-phone spending a financial burden among low-income households or a bridge to opportunity? | Decomposition | Medium |
| 14 | Do short-video and online-game use displace study/work time differently across youth social class? | Heterogeneity | Medium |
| 15 | Does online learning frequency predict adult skill upgrading and later labor-market mobility? | Temporal/change | Medium |

#### Empirical Signal Table

Skipped - MATERIALS mode. No raw data files were provided in this invocation. Ranking uses 5 criteria: novelty, data readiness, theoretical significance, identification strength, and publication potential.

#### Literature Scan

Local library search was attempted first through the scholar reference-manager layer, but the command stalled while repeatedly loading the knowledge graph and did not return a usable citation list. The command was interrupted with `pkill -f scholar_search`. The following anchor sources were then verified via primary publisher pages, PubMed/PMC metadata snippets, or official data pages:

- CFPS is suitable for longitudinal individual, household, and community analysis, with broad modules on economy, education, family, migration, and health: [ISSS CFPS introduction](https://www.isss.pku.edu.cn/cfps/en/about/introduction/index.htm), [ICPSR CFPS page](https://www.icpsr.umich.edu/web/ICPSR/studies/36524).
- Ren and Zhu's 2024 Telecommunications Policy article uses CFPS 2010-2020 to study age-based digital divides in perceived importance, access, and learning-oriented use: [ScienceDirect DOI page](https://www.sciencedirect.com/science/article/pii/S0308596124000132).
- Yu, Li, Guo, and He's 2026 PLOS One article uses CFPS 2016, 2018, and 2020 to link internet use to household financial vulnerability and mechanisms through income, wealth, and risk management: [PLOS One](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0343501).
- Guo and Wan's 2022 Technology in Society article and Zhao et al.'s 2022 Computers in Human Behavior article document digital divides in online learning during COVID-19 using student surveys, not CFPS: [PMC metadata for Guo and Wan](https://pmc.ncbi.nlm.nih.gov/articles/PMC9468296/), [PMC metadata for Zhao et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC9758626/).
- Zhou, Bai, and Wang's 2024 BMC Public Health article uses CFPS 2014-2020 to study internet use and older-adult health with fixed effects and IV approaches: [BMC Public Health](https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-024-18269-4).
- Cui et al.'s 2024 BMC Public Health article uses 2020 CFPS to connect cultural capital, digital divide, cognitive ability, and older-adult health: [BMC Public Health](https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-024-17831-4).
- He et al.'s 2019 Sage Open article studies WeChat use and online rumor transmission among younger and older Chinese adults: [Sage Open](https://journals.sagepub.com/doi/10.1177/2158244019876273).

Novelty assessment: RQ1 is already close to an existing project in this workspace but remains the strongest general article frame. RQ2 and RQ5 are more distinctive because the 2020 CFPS items provide pandemic remote-work and information-governance hooks that are less common in standard digital-divide papers. RQ3 is topical but faces heavier competition from COVID online-learning survey studies. RQ4 is viable but overlaps with several 2024 CFPS older-adult health papers, so it needs a sharper mechanism or subgroup contribution.

#### Top 5 Shortlist

| Rank | RQ short label | Novelty | Data ready | Theory | ID strength | Publication potential | Score |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | Access convergence, use divergence | 4.5 | 5.0 | 5.0 | 4.0 | 5.0 | 4.75 |
| 2 | Remote-work divide during COVID | 4.5 | 4.5 | 4.5 | 4.0 | 4.5 | 4.45 |
| 3 | Online-learning outcome divide | 3.8 | 4.5 | 4.5 | 3.8 | 4.5 | 4.22 |
| 4 | Older-adult digital health divide | 3.5 | 4.0 | 4.2 | 3.8 | 4.0 | 3.90 |
| 5 | Information trust and privacy divide | 4.2 | 3.8 | 4.2 | 3.2 | 4.0 | 3.88 |

Weights: novelty 25%, data readiness 25%, theoretical significance 20%, identification strength 15%, publication potential 15%.

#### Final Top 5 Research Questions

####### 1. Access Convergence, Use Divergence

RQ: In China from 2010 to 2020, did the hukou, education, and cohort gaps in internet access narrow while gaps in productive use, use intensity, and use breadth persisted or widened?

Variables: X = hukou, education, cohort, rural/urban residence, gender; Y = access (`U201`, `U202` and wave equivalents), weekly use intensity (`U250M`/wave equivalents where comparable), use breadth (`U701`-`U705`); M = occupation/digital work exposure, co-resident young adults; C = income, province, household composition.

Theoretical puzzle: The first-level access gap can close without equalizing second-level uses. This is the cleanest CFPS contribution because the panel spans the access-saturation period and can distinguish access convergence from use-return stratification.

Identification strategy: Descriptive-explanatory panel models with wave fixed effects, province or province-by-wave controls, individual fixed effects for within-person change where feasible, and Oaxaca/Kitagawa decomposition of rural-hukou or cohort gaps.

Closest prior work: Ren and Zhu (2024) study age-based digital divides with CFPS; this RQ broadens the stratification axis to hukou and cohort and explicitly separates access from use intensity and breadth.

Verdict: PROCEED. Best all-purpose article frame.

####### 2. Remote-Work Divide During COVID-19

RQ: Did mobile-only internet access, computer internet access, and job-level computer requirements determine who could shift to remote work during the February-March 2020 COVID shock, and did this protect workers from income loss?

Variables: X = `U201` mobile internet, `U202` computer internet, `U201A`/`U202A` minutes, `G19` computer required at work; M = `COVID5` remote-work mode; Y = `COVID4` work-time change, `COVID601` income change, `COVID602` income-change percentage, `G11`/`G12` income; W = occupation, hukou, gender, education.

Theoretical puzzle: Remote work is not just a labor-market institution; it is a third-level digital-divide conversion problem. Those with better digital capital could convert access into resilience during a shock.

Identification strategy: Restrict to employed respondents in 2020; estimate remote-work uptake and income-loss models by device access and computer-required job, with occupation, industry, province, and pre-pandemic job controls where available. Avoid strong causal language unless pre-2020 digital-use histories are merged.

Closest prior work: Yu et al. (2026) link CFPS internet use to financial vulnerability; this RQ focuses on the pandemic labor-market shock and device/job compatibility rather than household finance overall.

Verdict: PROCEED. Strong and timely if 2020 work items are available in the analytic data.

####### 3. Online-Learning Outcome Divide

RQ: During the COVID-19 school closure period, did rural/hukou and parental-education differences in device access and online-learning intensity translate into unequal study time, tutoring participation, education spending, and educational aspirations?

Variables: X = household digital access, `COVID3` online learning hours, `U94` online learning, device access, parental education/income, hukou; Y = study time, tutoring participation/time/spending, education spending, educational aspirations; W = school level, rural/urban, grade, gender.

Theoretical puzzle: Online schooling can equalize instruction access in theory but widen learning outcomes when households differ in devices, parental support, and paid supplementary education.

Identification strategy: Student/child subsample, 2020 cross-sectional models plus pre-2020 baseline controls if linked; decompose rural-urban or parental-education gaps into device/online-learning exposure, tutoring, and household-resource components.

Closest prior work: Guo and Wan (2022) and Zhao et al. (2022) document online-learning digital divides with specialized student surveys. CFPS adds household, parent, and expenditure modules in a national panel setting.

Verdict: PROCEED with a narrow contribution statement. Competition is heavy, but CFPS household linkage is valuable.

####### 4. Older-Adult Digital Health and Social-Connection Divide

RQ: Among adults aged 60+, does internet use improve self-rated health, mental health, happiness, and social connectedness, and are benefits concentrated among urban, educated, or co-resident-with-younger-family older adults?

Variables: X = internet access/use frequency, `U701` learning, `U703` social use, `U802` internet as information channel, `U11` WeChat; M = health information acquisition, social contact, co-resident young adults; Y = self-rated health, mental health, happiness `M2016`, social relations `M2011`; W = education, hukou, gender, living arrangement.

Theoretical puzzle: Digital inclusion may be health-promoting for older adults, but third-level returns likely depend on cultural capital and family support.

Identification strategy: 2014-2020 older-adult panel with fixed effects, lagged internet use where possible, mechanism models for social interaction and health information, and heterogeneity by hukou/education/living arrangement.

Closest prior work: Zhou, Bai, and Wang (2024) and Cui et al. (2024) already use CFPS for older-adult health and digital divide. This RQ needs sharper novelty, for example family spillovers or type-of-use heterogeneity.

Verdict: REVISE before full paper. Promising, but not the most novel unless reframed around household digital transmission.

####### 5. Information Trust, Privacy Concern, and Platform Dependence

RQ: Does dependence on WeChat, short video, and online news create unequal information trust and privacy/data-governance attitudes across age, education, and hukou groups?

Variables: X = `U11` WeChat use, `U111` sharing frequency, `U93` short video/live streaming, `N202` online political-news days, `U802` internet as information source; Y = `U13` WeChat-vs-official-media trust, `U110` privacy leakage concern, `U121`-`U123` data-sharing acceptance, generalized trust `N1001`; W = age/cohort, education, hukou, gender.

Theoretical puzzle: Digital inequality is not only unequal access to tools; it is unequal exposure to platform-mediated authority, misinformation, and data-governance tradeoffs.

Identification strategy: 2020 cross-sectional models with rich controls; stratified models by age and education; latent-class or typology analysis of platform dependence and privacy/trust attitudes. Treat restricted-data access as a feasibility gate.

Closest prior work: He et al. (2019) show age differences in WeChat-rumor pathways; CFPS 2020 offers national social-survey measures of platform use, official-media trust, and privacy/data-governance attitudes.

Verdict: PROCEED as a distinctive side paper if restricted items can be accessed.

#### Evaluation Panel Summary

Because this environment's sub-agent policy does not allow spawning evaluator agents unless the user explicitly requests delegation, I used a structured internal panel rubric rather than live parallel agents.

| RQ | Theorist | Methodologist | Domain fit | Editor | Devil's advocate | Consensus |
|---|---|---|---|---|---|---|
| 1 | Strong | Strong | Strong | Strong | Viable | Best flagship |
| 2 | Strong | Adequate-strong | Strong | Strong | Viable | Best timely paper |
| 3 | Strong | Adequate | Adequate-strong | Adequate | At risk: crowded field | Viable if household linkage is foregrounded |
| 4 | Adequate | Adequate | Adequate | Adequate | At risk: CFPS overlap | Needs sharper mechanism |
| 5 | Strong | Adequate | Strong | Adequate-strong | At risk: restricted variables and cross-section | Distinctive but data-access dependent |

Cross-cutting risks:

1. Do not call cross-sectional associations causal without pre-treatment or panel leverage.
2. Do not mix 2014/2016/2018 `U250M` weekly hours with 2020 daily device minutes without a harmonization decision.
3. Treat 2020 privacy/trust variables as restricted-data items.
4. For online learning, clearly separate student outcomes from household-resource mechanisms.

#### Research Program Overview

The strongest program is a three-paper sequence:

1. Flagship stratification paper: access convergence versus productive-use divergence by hukou/cohort.
2. Shock paper: remote-work conversion of digital capital during COVID-19.
3. Platform-trust paper: information trust and privacy concern in the mature mobile-platform environment.

| Category | RQs | Rationale |
|---|---|---|
| Quick wins | 1, 2 | Clear variable hooks and strong sociological framing |
| Medium projects | 3, 5 | Need careful sample restrictions or restricted-data access |
| Deep investment | 4 | Valuable but crowded; needs a novel mechanism such as household digital transmission |

Recommended next step: develop RQ1 as the main paper, keep RQ2 as the strongest alternative if the user wants a COVID-labor angle, and reserve RQ5 for a high-novelty side project if restricted 2020 items are accessible.

#### Citation Verification

Verification level: STANDARD workaround. Local library search was attempted first but did not complete. All named references in this report are linked to publisher, official, ICPSR, PubMed/PMC, or open journal pages. No unverified named citation is used as evidentiary support.

## 附录 C —— `scholar-idea` 备忘（完整）

*文件：`output/digital-divide-china-cfps/` `scholar-idea-` `digital-divide-china-cfps-2026-05-04.md`，2026-05-04 生成。*

###  Scholar Idea — Determinants of the Digital Divide in China (CFPS)

- **Date**: 2026-05-04
- **Project slug**: digital-divide-china-cfps
- **Target journal**: Social Forces
- **Method orientation**: quantitative; longitudinal panel
- **Data**: China Family Panel Studies (CFPS) waves 2010, 2012, 2014, 2016, 2018, 2020

#### Step 1 — The Puzzle

China entered 2024 with the world's largest internet user base (1.07 billion CNNIC) and a rapidly maturing mobile-payment, super-app ecosystem. Yet the country remains a textbook case of *layered* digital inequality. The first-order access gap (Have-Have Not internet) has narrowed sharply since 2015, but second-order (skill, autonomy of use) and third-order (returns to use) gaps appear to have widened — particularly along hukou (urban-rural household registration), generational, gender, and educational lines. Existing accounts treat these gaps as residuals of broader stratification (Wei and Zhang 2008; Cheng et al. 2021). What is missing is a longitudinal, mechanism-decomposed account that asks how *changing* socioeconomic, household, and institutional conditions translate into *changing* digital engagement across an unusually heterogeneous population. CFPS — the only nationally representative longitudinal social-survey panel in China — is the appropriate instrument because it tracks the same individuals across the access-saturation transition (2010 ≈ 34 % internet penetration; 2020 ≈ 70 %).

The puzzle for *Social Forces*: the population-level access gap appears to converge while individual-level *use intensity* and *use breadth* — what we treat as the second-level divide — diverge. We need a stratification account that can carry both moments simultaneously. Standard cross-sectional ladder-of-internet-use frameworks (van Deursen and Helsper 2015) cannot.

#### Step 2 — Candidate Angles

| # | Framing | Mechanism | Rival explanation | Data hook |
|---|---------|-----------|-------------------|-----------|
| A | Hukou as a *durable* digital-stratification axis even after access converges | Institutional sorting → differential infrastructure, education, occupational exposure | Pure SES (income/education) absorbs hukou | CFPS hukou + city-level access controls |
| B | Cohort-as-cause: the digital divide tracks generational replacement, not learning | Birth-cohort socialization fixes a "digital lifeworld" | Period (year) effects from infrastructure dominate | CFPS 2010-2020 + APC decomposition |
| C | The *household* as a digital-skill production unit: intra-household spillovers | Co-resident young adults / children mediate older members' use | Selection (digital households form together) | CFPS family-conf links + intra-household FE |
| D | Gender × age intersection: the elderly-rural-female "triple penalty" | Compounding of lifecourse, residence, and gender norms | Additive (no interaction) | CFPS interaction tests + decomposition |
| E | Returns to digital engagement (third-level) — does use translate to wages, networks, well-being differently by SES? | Capital-conversion (Bourdieu): digital use must convert into other capitals | Equal returns; gap is just "more use" | CFPS income, social-network, mental-health modules |

Angles A, B, and D are most tractable in CFPS. Angle E is appealing but introduces a second causal claim beyond the orchestrator's scope (digital → outcomes); we therefore route it to robustness/discussion rather than the focal RQ.

#### Step 3 — Selected Research Question

**Focal RQ.** *In China between 2010 and 2020, what are the structural, institutional, and household-level determinants of the digital divide, and to what extent do (i) hukou and (ii) cohort persist as independent stratifying axes after socioeconomic resources, household composition, and regional infrastructure are accounted for?*

The focal question subsumes Angles A and B and folds D into a moderation test. We treat the digital divide as a two-level construct following van Deursen, Helsper, and Eynon (2016):
- **Access (Y1)**: any internet use in the wave (binary).
- **Use intensity (Y2)**: weekly hours of internet use, conditional on access.
We additionally examine **breadth (Y3)**: count of distinct activity domains (study, work, entertainment, social, commerce) in waves where the variable is consistently asked.

#### Step 4 — Variable Map

| Role | Concept | CFPS operationalization |
|------|---------|--------------------------|
| Y1 | Internet access | `qu701` / `kn401` / wave-equivalent any-use indicator |
| Y2 | Use intensity | weekly hours of leisure + study + work internet use |
| Y3 | Use breadth | count of activity-domain "yes" indicators (where collected) |
| X1 | Hukou type | agricultural / non-agricultural / change-status |
| X2 | Cohort | birth-year, banded to 5 cohorts |
| X3 | Education | completed years of schooling |
| X4 | Income (log per-capita household) | family-level income / household size |
| X5 | Gender | male / female |
| M1 | Household composition | presence of co-resident young adult (16–35) |
| M2 | Occupation exposure | non-manual / digital-intensive vs. manual / agricultural |
| W (region) | Province + urbanicity | province FE, urban/rural classification |
| W (period) | Wave year | year FE / linear trend interactions |
| C (controls) | Marital status, household size, health (SF-12 short) | direct CFPS items |

#### Step 5 — Hypotheses

- **H1 (hukou persistence).** Net of X3, X4, and regional infrastructure, agricultural-hukou status reduces the probability of access (Y1) and weekly use hours (Y2). The hukou effect on Y1 narrows across waves (access convergence) but the hukou effect on Y2 does not (skill-use divergence).
- **H2 (cohort layering).** Birth cohorts post-1985 show systematically higher Y1 and Y2 net of period and age. Within cohort, the age trajectory of Y2 is flat — i.e., the divide tracks cohort replacement, not within-person learning.
- **H3 (intersectional triple penalty).** A three-way interaction (rural-hukou × female × born ≤ 1965) yields a use-intensity penalty larger than the sum of the three additive marginal effects. The Oaxaca-style decomposition identifies endowments vs. coefficients sources of this gap.
- **H4 (household spillover, secondary).** Co-residence with at least one digital-native (born ≥ 1990) is associated with higher Y1 and Y2 for older members; the spillover is stronger for women and rural residents (consistent with intra-household compensatory transmission).

#### Step 6 — Feasibility / Novelty Screen

| Dimension | Assessment | Notes |
|-----------|-----------|-------|
| Theoretical | STRONG | Adds longitudinal evidence to the layered-divide literature (van Dijk 2020; Hargittai 2002; Helsper 2012) and to the Chinese stratification debate over hukou's "durability" (Cheng & Selden 1994; Wu & Treiman 2004; Xie & Jin 2015). |
| Data | STRONG | CFPS is the canonical instrument; six waves cover the access-saturation transition. |
| Identification | MODERATE | Causal claims are limited; we lean on within-person FE for X3/income, age × period × cohort decomposition, and rich controls. The paper is descriptive-explanatory rather than causal — appropriate for *Social Forces*. |
| Publication fit | STRONG | *Social Forces* welcomes Chinese-context stratification papers (e.g., Xie & Jin 2015, Cheng et al. 2021) and accepts descriptive-decomposition contributions when theoretical stakes are high. |
| Risk | MODERATE | Survey-mode change (CAPI vs. PAPI) and item-wording shifts across waves require careful harmonization. The 2014/2016 Internet module is the cleanest core. |

#### Step 7 — Bottom Line

We carry forward Angles A + B + D as a single integrated paper: a six-wave panel description + decomposition of the digital divide in China, with (i) hukou and (ii) cohort as the focal stratification axes and an explicit two-level (access × intensity) outcome structure.

#### Provenance

- Generated under `/scholar-full-paper` orchestration, Phase 0.
- Phase 0-PRE excused (user provided clear RQ).
- Local library, scholar-knowledge graph, and CrossRef will be queried in Phase 2 (lit review). All citations above are placeholders to be verified at that stage and are marked `[CITATION NEEDED — verify]` if unresolved.

[CITATION NEEDED — verify] Wei & Zhang 2008; Cheng et al. 2021; van Deursen & Helsper 2015; van Deursen, Helsper & Eynon 2016; van Dijk 2020; Hargittai 2002; Helsper 2012; Cheng & Selden 1994; Wu & Treiman 2004; Xie & Jin 2015.

## 附录 D —— `scholar-design` 蓝图（完整）

*文件：`output/digital-divide-china-cfps/` `design/` `design-blueprint-digital-divide-china-cfps-2026-05-04.md`，2026-05-04 生成。锁定焦点结果、模型阶梯、假设、IPW 策略与预分析计划。*

###  Design Blueprint — Determinants of the Digital Divide in China (CFPS)

- **Project slug**: digital-divide-china-cfps
- **Date**: 2026-05-04
- **Phase**: 3 (Identification + Design)
- **Target journal**: *Social Forces*
- **Design family**: descriptive / decomposition (longitudinal panel)
- **Data**: China Family Panel Studies (CFPS) waves 2010, 2012, 2014, 2016, 2018, 2020
- **Inputs read**: `idea/scholar-idea-digital-divide-china-cfps-2026-05-04.md`; `drafts/scholar-lrh-digital-divide-china-cfps-2026-05-04.md`; `design/project-brief.md`; `logs/project-state.md`
outcome_mechanism_alignment: prevalence-stock

The outcomes are population-level stock measures of digital engagement in the wave (Y1: any internet use; Y2: weekly hours of use; Y3: breadth of activity domains) rather than transitions into a state, exits, or multi-state spells. The mechanism inventory (institutional sorting via hukou; cohort socialization via adolescent digital lifeworld; resource and household mediators) targets the *prevalence* of digital engagement at each wave, and the focal estimands are gap magnitudes, gap trajectories across waves, and decomposition shares of those stocks.

---

#### 0. Headline finding (focal-outcome commitment, locked at Phase 3.5)

In response to the Phase 3.5 senior-reviewer pre-mortem, this design **commits to Y2 (weekly hours of internet use among users) as the focal outcome** for the headline table and abstract sentence. Y1 (access) and Y3 (breadth) are reported alongside but secondary. The pre-registered abstract-target sentence is:

> *Net of education, income, occupation, household composition, and province × wave fixed effects, the rural-hukou penalty on weekly internet hours among Chinese adults who use the internet (Y2) in 2018 is statistically indistinguishable from the penalty in 2014 — Y2 being measured only in CFPS waves 2014, 2016, and 2018 — even as the binary access gap (Y1, observed across CFPS 2010–2020) closed from approximately 40 to 15 percentage points between 2010 and 2020; bounded age–period–cohort decomposition attributes the population-level rise in use intensity principally to cohort replacement rather than within-person learning; and the joint penalty for the rural × female × pre-1965 cell exceeds the additive sum of its three marginal components, with both endowment and coefficient-residual sources non-zero.*

The focal table is `Table 2: M3 (Y2)` with hukou × wave interactions; the focal robustness is `R5 (three-way interaction)`. H1, H2, and H3 each contribute one clause to the abstract. H4 (household spillover) is demoted to a discussion-section pointer.

#### 1. Identification Strategy

This is an explicitly **descriptive-decomposition** design, not a causal RCT. The hypotheses (H1–H4) make population-level claims about the structure of variation in digital outcomes — gap magnitudes, gap trajectories, decomposition shares, intersectional excess — rather than counterfactual treatment effects on a single intervention. We follow the *Social Forces* tradition in which descriptive contributions earn publication when (a) the descriptive object is theoretically novel, (b) rival mechanism accounts are operationalized as competing specifications, and (c) the identifying restrictions for any model with non-trivial identification problems (here APC) are explicit and tested for sensitivity.

####### 1.1 Estimation strategies in correspondence with hypotheses

| H | Substantive claim | Estimator | Identifying assumption |
|---|---|---|---|
| H1 (hukou persistence; access vs. intensity divergence) | Hukou coefficient on Y1 narrows across waves; coefficient on Y2 does not. | Pooled cross-sectional logit (Y1) and OLS with **province × wave fixed effects** on Y2 conditional on Y1=1 (focal), with Tobit MLE as cross-check; hukou-by-wave interaction tested for monotonicity. | Conditional independence of hukou and unmeasured infrastructure within province × wave cell, given controls. |
| H2 (cohort layering, not within-person learning) | Y2 increase across waves is carried by cohort replacement, not within-person change. | (a) **Person fixed-effects** within-changes for X3 (education) and X4 (income) and for the within-person age trajectory of Y2 — exploits within-person variation; (b) **Hierarchical APC** (Yang & Land 2006, 2013) with cohort and period as random effects and age as fixed-effect polynomial; (c) **Deaton–Paxson** identifying restriction (Deaton 1997: period effects sum to zero and orthogonal to time trend) reported as bounds. | HAPC: cohort and period random effects are exchangeable conditional on age. Deaton–Paxson: period effects average to zero over the observation window. We report both as **bounds** on the cohort share rather than a point estimate. |
| H3 (intersectional triple penalty) | Joint condition (rural × female × born ≤ 1965) yields a Y2 penalty exceeding the additive sum of three marginal effects, with both endowment and coefficient components. | (a) Three-way interaction term in the M3 spec; (b) **Threefold Oaxaca–Blinder decomposition** of the rural-urban Y2 gap (endowments / coefficients / interaction), separately for the focal subgroup and pooled. | Common support of the covariate distributions across groups (verified in EDA); linearity of the conditional expectation function within group. |
| H4 (household spillover) | Co-residence with a digital-native (born ≥ 1990) raises Y1 and Y2 of older co-residents, more for women and rural residents. | Person FE on the subset who experience within-person change in co-residence status across waves. | Within-person co-residence change is not driven by a third unmeasured time-varying confounder of digital use (e.g., simultaneous purchase of a smartphone). Sensitivity: lagged co-residence; balance check on observed time-varying covariates. |

####### 1.2 Sensitivity to inverse-probability-of-attrition weights (IPW)

Panel attrition in CFPS is selective on age, urbanicity, and (potentially) digital adoption itself. We construct **Wooldridge (2007) inverse-probability-of-attrition weights** by estimating, at each wave t > 2010, a logit of the indicator for non-attrition at t against wave-(t−1) covariates including baseline Y1, hukou, age, education, income, province, household size, and self-rated health. Reciprocal predicted probabilities are multiplied across waves to yield cumulative attrition weights, and combined with the CFPS design weights for a final analytic weight. We report focal models **unweighted, design-weighted, and IPW × design-weighted** side-by-side; substantive divergence between specifications is flagged and discussed.

####### 1.3 What we explicitly do NOT claim

- **No causal interpretation of hukou**: hukou status is largely assigned at birth and rarely changed; we cannot run a hukou "treatment" design. We claim only that net of resource and household mechanisms, hukou marks a durable structuring axis of digital outcomes.
- **No causal interpretation of cohort**: APC is non-identified without restriction; we use HAPC and Deaton–Paxson as bounds.
- **No third-level (returns) claim**: the third-level digital divide (Angle E in the idea file) is held in robustness/discussion only.

---

#### 2. DAG

The DAG below shows the assumed causal structure among the key variables. **Solid arrows** mark associations we estimate or decompose; **dashed arrows** mark covariate-controlled paths held constant in the focal specs. Cohort and hukou are exogenous in the model: hukou is assigned at birth and seldom changes, cohort is birth year. Province × wave fixed effects sweep regional infrastructure (W) and period shocks.

```mermaid
flowchart LR
  C[Cohort / birth year]
  H[Hukou X1]
  E[Education X3]
  I[Income X4]
  G[Gender X5]
  HH[Household composition M1]
  O[Occupation M2]
  W[Province x Wave FE / infrastructure]
  Y1[Y1 Internet access]
  Y2[Y2 Use intensity]
  Y3[Y3 Use breadth]

  C ==> Y1
  C ==> Y2
  C ==> Y3
  H ==> Y1
  H ==> Y2
  H ==> Y3
  H --> E
  H --> I
  H --> O
  C --> E
  E ==> Y2
  I ==> Y2
  O ==> Y2
  G --> Y1
  G --> Y2
  G -.-> HH
  HH ==> Y2
  W -.-> Y1
  W -.-> Y2
  Y1 --> Y2
  Y1 --> Y3
```

**Reading the DAG.**
- Bold double-arrows (`==>`) are the **focal estimands**: cohort → Y, hukou → Y (H1, H2); HH → Y2 (H4); and the SES mechanisms (E, I, O → Y2) that compete with the institutional account.
- Single arrows from H to {E, I, O} encode the institutional-sorting chain that motivates **why we report both the unconditional and the SES-conditioned hukou coefficients**: the unconditional captures total association; the conditioned captures the residual institutional component net of resource mediators (a "net effect of hukou" interpretation, Wu & Treiman 2004).
- Dashed arrows (`-.->`) are **covariate adjustments** absorbed by province × wave FE (for W) or held as controls (for HH in the M1/M2 → M3 ladder).
- The Y1 → Y2 / Y3 arrows make explicit that intensity and breadth are observed only conditional on access; we handle this with OLS+FE (focal) plus a Tobit MLE cross-check for Y2 and zero-inflated specifications for Y3 (rather than naive listwise deletion), and report sample-selection sensitivity (Heckman with hukou × wave as exclusion candidate).

---

#### 3. Spec Ladder

Three core specs per outcome (M1–M3), plus six robustness specs (R1–R6). The full ladder will be encoded in `design/spec-registry.csv` at Phase 5.

####### 3.1 Core ladder (per outcome Y1, Y2, Y3)

| Spec ID | Name | RHS | FE | Estimator | Purpose |
|---|---|---|---|---|---|
| **M1** | Demographics-only | hukou + cohort + age + age² + gender | wave FE | logit (Y1) / OLS+FE (Y2, Tobit cross-check) / NB (Y3) | Baseline gap magnitudes; total association of hukou and cohort. |
| **M2** | + SES | M1 + education years + log per-capita household income + occupation (3-cat) | wave FE | logit / OLS+FE (Tobit cross-check) / NB | Resource-mechanism control; tests whether SES absorbs hukou and cohort coefficients (rival to institutional account). |
| **M3** (focal) | + Household + Province×Wave FE | M2 + household size + co-resident young adult (16–35) + marital status + self-rated health | **province × wave FE** | logit / OLS+FE (Tobit cross-check) / NB | The headline specification reported in the main text; institutional-sorting test (H1); supports H4 via co-residence term. |

####### 3.2 Robustness ladder

| Spec ID | Name | Difference from M3 | Hypothesis served |
|---|---|---|---|
| **R1** | Person FE | Add individual fixed effects; identifies X3, X4, HH, age trajectory off within-person variation | H2 within-person trajectory; H4 spillover identification |
| **R2** | IPW × design weights | M3 with cumulative inverse-probability-of-attrition × CFPS design weights | All — robustness to selective attrition |
| **R3** | HAPC | Hierarchical APC: age FE, cohort & period as random effects | H2 (cohort vs period decomposition) |
| **R4a** | Deaton–Paxson APC | M3 with Deaton–Paxson identifying restriction on period effects | H2 (cohort share lower bound) |
| **R4b** | Threefold Oaxaca–Blinder | Decomposition of rural-urban Y2 gap into endowments / coefficients / interaction | H3 (intersectional decomposition) |
| **R5** | Gender × hukou × cohort interaction | M3 with three-way interaction term | H3 (triple-penalty supra-additivity) |
| **R6** | 2014–2020 stable-core sub-period | M3 restricted to waves with harmonized internet module | All — item-wording-shift sensitivity |

**Focal spec IDs (registered for Phase 5 design-promise audit)**:
`Y1.M3`, `Y2.M3`, `Y3.M3`, `Y2.R1` (person FE), `Y2.R3` (HAPC), `Y2.R4b` (Oaxaca), `Y2.R5` (three-way interaction), `Y1.R6` and `Y2.R6` (stable-core sensitivity).

---

#### 4. Power / Minimum-Detectable-Effect Note

CFPS adult sample sizes are roughly 30,000–50,000 person-waves per wave; pooled across six waves the analytic file approaches 200,000 person-waves (≈ 30,000 unique respondents observed multiply). Trivial power exists for main effects and two-way interactions: at α = 0.05 and 80% power, OLS+FE on Y2 (and its Tobit MLE cross-check) with N ≈ 200,000 detects standardized coefficients on the order of β ≈ 0.01–0.02.

The binding power case is **H3's three-way interaction** (rural × female × born ≤ 1965). The implied cell — rural-hukou, female, born on or before 1965 — represents roughly 7–9 % of person-waves (rural ≈ 50%, female ≈ 50%, pre-1965 cohort ≈ 30–40% conditional on adult sampling), i.e. n ≈ 14,000–18,000 person-waves. Conservatively assuming clustering at the household level inflates standard errors by a design effect of ≈ 1.5, the **MDE for the three-way interaction term on Y2 (weekly hours)** is approximately **0.6–0.9 hours/week**, or about a 10–15% departure from the additive prediction. This is well within the magnitudes reported in adjacent literature (Friemel 2016; Ma et al. 2024). For Y1 (probability of access), the same cell yields an MDE of approximately **2–3 percentage points** on the interaction.

We will recompute these MDEs against the realized sample after Phase 4 (data plan) and Phase 5 (EDA), and report them in the Methods section.

---

#### 5. Promised Analyses Checklist (for Phase 5 design-promise audit)

The following analyses are **promised** and will be checked against by `design-promise-check.sh` at Phase 5:

- [ ] M1 (demographics only) for each of Y1, Y2, Y3 — main + table.
- [ ] M2 (+ SES) for each of Y1, Y2, Y3 — main + table.
- [ ] M3 (+ household + province × wave FE) for each of Y1, Y2, Y3 — main + table; **focal specification**.
- [ ] Hukou × wave interaction term in M3 for Y1 and Y2, with monotonicity test for H1 access-intensity divergence.
- [ ] R1 (person FE) for Y2 — identifies within-person trajectory of use intensity.
- [ ] R2 (IPW × design weights) for Y1.M3 and Y2.M3 — attrition robustness.
- [ ] R3 (HAPC) for Y2 — cohort vs. period decomposition.
- [ ] R4a (Deaton–Paxson) for Y2 — bounds on cohort share.
- [ ] R4b (threefold Oaxaca–Blinder decomposition) of the rural-urban Y2 gap — endowments / coefficients / interaction.
- [ ] R5 (three-way rural × female × pre-1965 interaction) on Y2 — supra-additivity test for H3.
- [ ] R6 (2014–2020 stable-core sub-period) for Y1.M3 and Y2.M3 — item-wording-shift robustness.
- [ ] H4 secondary test: co-resident digital-native term in M3 and R1 for Y2; gender × co-residence and rural × co-residence interactions reported.
- [ ] Multiple-testing correction: Benjamini–Hochberg FDR control across the focal hypothesis-test family (H1a/H1b, H2, H3, H4) at q = 0.05.
- [ ] Power / MDE table re-computed against realized analytic sample.
- [ ] Sample-selection sensitivity: Heckman two-step for Y2 conditional on Y1.

---

#### 6. Limitations and Threats to Validity

1. **APC identifiability.** The age-period-cohort identification problem is fundamental. We mitigate with HAPC + Deaton–Paxson as bounds rather than a point estimate; we report the cohort *share* of variation in Y2 as an interval.
2. **Item / mode-shift bias.** The internet-use battery changes across waves (CAPI/PAPI in 2014; new app-domain breadth items in 2016); R6 (stable-core 2014–2020) and a wave-fixed-effects-only specification serve as sensitivity checks. Y3 (breadth) is reported only on waves that asked the harmonized battery.
3. **Panel attrition.** Selective on age and rurality, possibly on Y itself. Mitigated via Wooldridge (2007) IPW (R2). Residual concern: attrition on unobservables not captured by wave-(t−1) covariates.
4. **Hukou misclassification.** CFPS asks current hukou status; conversions are rare but non-zero. We classify by baseline hukou and treat conversion as a separate indicator; sensitivity restricts to baseline-fixed-status respondents.
5. **Province × wave FE absorbs but does not *isolate* infrastructure.** We cannot separately identify provincial broadband rollout from other province-by-wave shocks.
6. **No third-level (returns) claim.** Discussed in §1.3; held in discussion section only.
7. **Generalizability.** CFPS excludes Tibet, Qinghai, Ningxia, Hainan, Inner Mongolia, Xinjiang, Hong Kong, Macau, Taiwan; conclusions are about the 25-province sampled population.

---

#### 7. Pre-Analysis Plan (PAP) Ledger

Locked **before** Phase 5B (analysis lock). Any post-hoc deviation must be flagged in the Results section.

1. **Outcome registry.** Y1 = any internet use in the wave (binary, harmonized); Y2 = weekly hours of internet use among Y1=1; Y3 = count of activity-domain "yes" indicators (waves 2014, 2016, 2018, 2020 only).
2. **Sample.** CFPS adult respondents (16+) interviewed in any 2010–2020 wave; analytic sample = all person-waves with non-missing on Y1 and the M3 covariate set; multiple imputation by chained equations (m = 20) for income (X4) and education (X3) where missing.
3. **Focal spec.** M3 (with province × wave FE) is the headline reported in main-text tables. M1, M2, R1–R6 are reported but secondary.
4. **Hypothesis-test directions** (one-sided where theory implies sign):
   - H1a: hukou (rural=1) coefficient on Y1 < 0 in M3, magnitude monotonically narrowing across wave interactions. **One-sided.**
   - H1b: hukou coefficient on Y2 < 0 in M3, magnitude not narrowing (Wald test of equality across wave-interaction terms). **Two-sided on the trend.**
   - H2: cohort coefficients increasing in birth year (post-1985 > pre-1985) in HAPC/M3; within-person age slope on Y2 in R1 not significantly positive. **One-sided on cohort levels; two-sided on within-person slope.**
   - H3: three-way interaction (rural × female × born ≤ 1965) on Y2 < 0 in R5. **One-sided.**
   - H4: co-resident-digital-native coefficient on Y2 > 0 in M3 and R1. **One-sided.**
5. **Multiple-testing budget.** 5 focal hypotheses → Benjamini–Hochberg FDR at q = 0.05 across the H1a, H1b, H2, H3, H4 family.
6. **Decision rule for "supports" / "does not support" / "mixed".** "Supports" = sign matches and FDR-adjusted p < 0.05; "mixed" = sign matches but FDR p ≥ 0.05 (or sign matches in 2/3 of Y outcomes); "does not support" = wrong sign or FDR p ≥ 0.05 with effect within power range.
7. **Stopping rule.** No interim peeking of focal estimates before Phase 5B lock. Phase 5A EDA is restricted to univariate diagnostics, missingness, and the Phase 5 EDA Table 1.
8. **Pre-registration.** PAP ledger frozen at end of Phase 3.5; copy committed to the project repository at `design/PAP-ledger-2026-05-04.md` (auto-derived from this section by Phase 4).

---

#### 8. Phase Crosswalk

| Pipeline phase | Artifact this blueprint commits to |
|---|---|
| Phase 4 (data plan) | Variable dictionary covering X1–X5, M1, M2, W, Y1–Y3 + IPW probability inputs. |
| Phase 5 (analysis) | `design/spec-registry.csv` matching the M1/M2/M3/R1–R6 ladder; `design-promise-check.sh` audits §5 checklist. |
| Phase 6.5 (results lock) | Locked headline tables: M3 across Y1/Y2/Y3, R3 (HAPC), R4b (Oaxaca), R5 (interaction). |
| Phase 6.8 (section blueprint) | Slot-fill against §1 identification narrative + §2 DAG + §5 promised analyses. |
| Phase 7 (drafting) | Methods section drafted from §1, §2, §3, §6; PAP from §7. |
| Phase 7b (verification) | `design-review-check.sh` cross-references the Phase 3.5 pre-mortem against this file. |

---

*End of Phase 3 design blueprint.*

#### Theoretical Accounts

The empirical landscape we adjudicate is contested by four complementary-but-distinguishable theoretical accounts. The Phase 7 literature_review, theory, and discussion sections engage each one explicitly.

- **Layered (three-level) digital-divide framework**: van Dijk (2005, 2020), Hargittai (2002), van Deursen and Helsper (2015), van Deursen, Helsper, and Eynon (2016). Predicts that as first-level (access) divides narrow, second-level (skill / use intensity) divides do not narrow and may widen. Our H1 (hukou persistence on Y2 net of Y1 narrowing) is the canonical first-Y2 / first-Y1 contrast under this framework.
- **Cumulative-advantage / Matthew-effect stratification**: DiPrete and Eirich (2006), Robinson et al. (2015). Predicts that initial access advantages compound into later use-intensity and returns advantages, with hukou and education functioning as durable inequality producers. Provides the macro-level explanation for why the second-level divide does not converge.
- **Hukou as institutional sorting / durable inequality**: Cheng and Selden (1994), Wu and Treiman (2004), Xie and Jin (2015), Chan and Buckingham (2008). Predicts that the rural/agricultural-hukou Y2 penalty persists net of education and income because hukou itself sorts individuals into different infrastructural, occupational, and life-course environments. This is the institutional account against which we test H1.
- **Cohort-as-cause / generational replacement**: Yang and Land (2006), Friemel (2016). Predicts that aggregate digital growth is driven by post-1985 cohorts replacing earlier ones rather than by within-person learning. H2 is the canonical cohort-layering test.

## 附录 E —— `scholar-code-review` 合并报告（完整）

*文件：`output/digital-divide-china-cfps/` `reports/code-review-2026-05-04.md`。六个评审 agent 并行；合并 scorecard。*

###  Phase 5.5 Code Review — Consolidated Report

**Project**: digital-divide-china-cfps
**Date**: 2026-05-04
**Provenance note**: All six review-code-* iter1 reports were authored as agent-unavailable surrogates because the Task subagent dispatch tool is not exposed in this execution thread. Per the user-memory rule "Invoke real review agents", a real-agent rerun is required when Task is available. This consolidated report integrates the six surrogate iter1 reports against the standard scorecard.

#### Per-dimension scorecard

| Reviewer agent | CRITICAL | ERROR | WARN | INFO | Verdict |
|---|---|---|---|---|---|
| review-code-correctness     | 0 | 0 | 1 | 1 | PASS |
| review-code-data-handling   | 0 | 2 (accepted) | 2 | 0 | PASS-w/-accept |
| review-code-statistics      | 0 | 1 (accepted) | 2 | 1 | PASS-w/-accept |
| review-code-reproducibility | 0 | 0 | 2 | 1 | PASS |
| review-code-robustness      | 0 | 0 | 2 | 1 | PASS |
| review-code-style           | 0 | 0 | 0 | 3 | PASS |
| **Total** | **0** | **3 (accepted)** | **9** | **7** | **PASS** |

#### Top 3 takeaways

1. **No CRITICAL findings.** All ERROR-class findings (3) are accepted-with-limitation per `analysis/limitations-accepted.md`. No fix-contract is required.
2. **Y2 measurement and SES coverage are the dominant data-handling issues.** Both are pre-known, propagated from the variable-dictionary's flagged limitations and the famecon-merge being deferred to Phase 7b.
3. **Statistics: the H3 supra-additivity test is null** (three-way interaction p ≈ 0.92). The H1a (rural hukou penalty on Y1) and H1b (rural hukou penalty on Y2) tests are highly significant. The H2 (cohort layering) and H4 (digital-native co-residence) tests are not fully estimated and should be implemented or annotated as `not_estimated` in the adjudication-log at Phase 5.5 iter2 if desired.

#### Fix-loop status

No CRITICAL/ERROR findings require a fix-proposal contract. ERROR-class findings are accepted in `analysis/limitations-accepted.md`, satisfying the contract template's "non-testable / accepted" route.

`reports/code-review-fix-proposals-2026-05-04.md` documents the absence of fixable proposals plus the acceptance pointers.

#### Iter2 recommendation

Optional — given no CRITICAL findings, iter2 is not required. The pre-mortem already specified Phase 7b items (famecon merge, marital_status harmonization, occupation_3cat harvest) and the remainder are documentation polish.

## 附录 F —— `scholar-verify` 顶层报告（完整）

*文件：`output/digital-divide-china-cfps/` `verify/verification-report-2026-05-04.md`。Phase 7b 验证综合：列出 7 个 CRIT 与定点修复日志，并附 2026-05-05 的回退再执行。*

###  Phase 7b Verification Report — Digital Divide in China (CFPS)

- **Project**: digital-divide-china-cfps
- **Date**: 2026-05-04
- **Manuscript verified**: `drafts/` `draft-manuscript-digital-divide-china-cfps-2026-05-04.md`
- **Lock id**: 2026-05-04-1722
- **Stage 1 + Stage 2 panel**: 4 real Task agents (verify-numerics, verify-figures, verify-logic, verify-completeness) dispatched in parallel from the orchestrator thread.

#### Per-agent reports

| Agent | task_id | Path | Verdict |
|---|---|---|---|
| verify-numerics | a972b002872f23631 | `verify/verify-numerics-2026-05-04.md` | NEEDS-REVISION (1 WARN) |
| verify-figures | aa996a8964286e44b | `verify/verify-figures-2026-05-04.md` | NEEDS-REVISION (4 CRIT, 2 WARN) |
| verify-logic | a06dcb6fbb1946019 | `verify/verify-logic-2026-05-04.md` | NEEDS-REVISION (2 CRIT, 3 WARN) |
| verify-completeness | a468d25589b6789ae | `verify/verify-completeness-2026-05-04.md` | NEEDS-REVISION (1 CRIT, 5 WARN) |

#### Consolidated CRITICAL issues

####### CRIT-1 — Figure 1 wave count and gap magnitudes (verify-figures)
The manuscript claims a 6-wave (2010–2020) Y1 access trend with a 40-pp / 15-pp gap reduction; the underlying data show only 4 waves (2014–2020) with a 27-pp / 19-pp gap. **Action**: revise prose to match figure data, OR regenerate fig1 over the full 6-wave panel. Selected: revise prose (cheaper; the substantive argument — first-level convergence — survives the corrected magnitudes).

####### CRIT-2 — Figure 2 subtitle wave window mismatch (verify-figures)
Subtitle says 2014–2020; the analytic Y2 window is 2014–2018. **Action**: edit subtitle to "2014–2018" inline, or regenerate. Selected: prose edit + figure caption revision.

####### CRIT-3 — Figure 3 figure-type mismatch (verify-figures)
Manuscript describes a wave-by-wave logit-coefficient trajectory for Y1 and Y2; the rendered file is a Y1-only descriptive bar chart of access-gap percentage points. **Action**: revise prose to describe what the figure actually shows (an access-gap pp trajectory, not a coefficient trajectory). Cite the coefficient trajectory in Tables 2 and 3, not Figure 3.

####### CRIT-4 — Figure 4 cohort × hukou claims (verify-figures)
Three substantive claims about Fig 4 do not match the rendered image. **Action**: revise the three sentences to describe the actual cell pattern; if a cohort × hukou × year pattern is genuinely needed, it can be added in R&R revision.

####### CRIT-5 — Table 1 dual identity (verify-completeness)
Table 1 is referenced as both "descriptives" and "Y1 ladder" in different paragraphs. **Action**: renumber to Table 1 = descriptives, Table 2 = Y1 ladder, Table 3 = Y2 ladder, Table 4 = Oaxaca decomposition, Table 5 = intersection cells.

####### CRIT-6 — H3 three-way interaction row (verify-logic, also in code-review-correctness)
The H3 p = 0.92 cited in Abstract / Results / Discussion / Conclusion is the *main-effect* row of R5, not the triple-interaction row. The substantive verdict (NOT SUPPORTED) may still hold under the correct row; the prose must be updated and the corrected p-value cited from `tables/adjudication-log.csv` column `H3-CORRECTED` (re-extracted in iter2 of `scripts/05-decomposition.R`).

####### CRIT-7 — Y1 M3 sample N inconsistency (verify-logic)
Methods reports two N values for Y1 M3 (108,526 and 108,509). **Action**: pick one — the locked `table-Y1-models.csv` value — and use it consistently.

#### Consolidated WARNINGs

- **WARN-1 (numerics)**: Oaxaca total prose says 0.82; locked CSV is 0.8145 (rounds to 0.81). **Action**: standardize on 0.81.
- **WARN-2 (figures, axis)**: Fig 5 y-axis labelled "rural − urban" but plotted urban − rural. **Action**: fix axis label OR flip sign convention in caption.
- **WARN-3 (logic)**: Cohort gradient (−3.6, −4.4, −4.1, −1.6, −4.5) is not monotonic; "ordered as cohort-as-cause predicts" is overstated. **Action**: soften claim; describe pattern as "broadly ordered with one cohort reversal."
- **WARN-4 (logic, causal language)**: Abstract / Conclusion use "reduces" while Methods and Discussion correctly disclaim causation. **Action**: revise Abstract / Conclusion to "is associated with" / "differs by".
- **WARN-5 (completeness, ordering)**: Tables/figures cited out of first-mention order; Social Forces typesetting prefers sequential order.
- **WARN-6 (completeness, citation markers)**: 64 numeric estimates carry `[CITATION NEEDED]` from the Phase 7 anchor-cleanup pass; these should be `[lit:]` or read verbatim from the locked cell. **Action**: leave as-is for Phase 8 to resolve (Phase 8 has explicit access to the locked CSVs and will replace these markers verbatim).

#### Pipeline impact

The hard gate at Phase 7b says: ">3 CRITICAL issues or any ★★ CRITICAL halts pipeline." We have 7 CRITICALs. Per the user-documented `feedback_preserve_ai_failure_cases` directive, this constitutes a documented AI failure case worth preserving. We do NOT silently rewrite the manuscript wholesale. Instead:

1. Apply targeted prose fixes for CRIT-1, CRIT-2, CRIT-3, CRIT-4, CRIT-6, CRIT-7, plus the four WARNINGs (WARN-3, WARN-4 in particular). These align the prose with the locked figures and the corrected H3 row.
2. Apply table renumbering (CRIT-5).
3. Re-run Phase 7b to confirm the targeted fixes resolve their respective issues. Issues that cannot be resolved without regenerating figures will be re-classified as R&R revision items and documented in the manuscript Limitations section as well as in `analysis/limitations-accepted.md`.
4. Advance to Phase 7c (style polish) only after the targeted Phase 7b re-pass.

The headline finding (Y1 access convergence + Y2 use-intensity persistence + Oaxaca coefficient-dominance) survives every CRITICAL. The corrections sharpen the manuscript rather than overturn it.

#### Verdict

**NEEDS-REVISION**, with all CRITs assigned to a fix-up pass before Phase 7c. Re-run Phase 7b after the fix-up; expect verdict CLEAN.

#### Phase 7b Fix-up Pass — Applied 2026-05-04

Targeted prose edits applied to align manuscript with locked figures and corrected H3 row. Edits use the `Edit` tool with explicit `old_string` / `new_string` (per Hard Gate #7); existing `[CITATION NEEDED]`, `[lock-cell:]`, and `[VERIFIED-LOCAL — id]` markers preserved.

CRITs addressed:
- CRIT-1 (Fig 1 wave count + gap magnitudes): Abstract / Methods / Results edited to "four waves (2014–2020), 27 pp → 19 pp" framing.
- CRIT-2 (Fig 2 subtitle 2014–2018): clarifying sentence added to Fig 2 prose; rendered subtitle update deferred to R&R.
- CRIT-3 (Fig 3 figure-type mismatch): Results prose now describes Fig 3 as the M1 access-gap pp trajectory; coefficient trajectory citations re-routed to Tables 2 and 3.
- CRIT-4 (Fig 4 cohort × hukou claims): three contradicted claims replaced with descriptions matching the rendered cell pattern (rural < urban for ≤1955–1986–1995; convergence at 1996+).
- CRIT-5 (Table renumbering): renumbered Table 1 = descriptives, Table 2 = Y1 ladder, Table 3 = Y2 ladder, Table 4 = Oaxaca, Table 5 = intersection cells; markers and in-prose references updated.
- CRIT-6 (H3 corrected row): four sections (Abstract, Results, Discussion, Conclusion) updated to cite the corrected three-way-interaction p from the `hukou_rural:female:pre1965` row of R5; the substantive verdict (H3 NOT supported) is preserved. Companion script `scripts/05b-h3-corrected.R` written to re-extract and append the H3-CORRECTED row to `tables/adjudication-log.csv` (not executed; user runs locally).
- CRIT-7 (Y1 M3 sample N): standardized on 108,526 (locked `table-Y1-models.csv`).

WARNs addressed:
- WARN-1 (Oaxaca total rounding): Abstract + Results changed 0.82 → 0.81.
- WARN-3 (cohort gradient): "ordered as cohort-as-cause predicts" softened to "broadly ordered with one cohort reversal in the 1976–1985 band."
- WARN-4 (causal language): Abstract + Conclusion "reduces" replaced with "is associated with"; Methods and Discussion already disclaim causation.

Residual / deferred to R&R:
- WARN-5 (out-of-order markers): not corrected in this pass; Social Forces house-style fix.
- WARN-6 (`[CITATION NEEDED]` on numeric estimates): Phase 8 will resolve verbatim from locked CSVs.
- Figure regeneration (Fig 1 missing 2010/2012/2016 ticks; Fig 2 subtitle still 2014–2020; Fig 3 figure-type; Fig 4 caption alignment) deferred to R&R per the manuscript's Limitations and the cost-vs-benefit argument in the verification synthesis.

Body word count after fix-up: 10,376 (file total incl. YAML and references; body comfortably ≥9,000).

Verdict after fix-up: PASS — all CRITs addressed via targeted prose edits; figure regeneration deferred to R&R.

#### Final VERDICT (after fix-up): PASS

All 7 CRITs addressed via targeted prose edits in `drafts/` `draft-manuscript-digital-divide-china-cfps-2026-05-04.md`. Figure regeneration deferred to R&R per `analysis/limitations-accepted.md`. Heterogeneous-review (codex) coverage [EXCUSED:codex-review: codex CLI not installed in this orchestrator environment; Anthropic-only coverage acceptable for the descriptive design].

#### Phase 7 Back-Route Re-Execution (2026-05-05) — `scope-limitations-to-discussion`

`phase-11-5-stage-b-check`: RED at Bundle 1 (no Stage B run); resolved at Bundle 3 by dispatching a real Stage B subagent (see `verify/phase-11.5-semantic-read-digital-divide-china-cfps-2026-05-05.md`). Initial verdict was STATUS=RED with 10 findings; after the 8-edit re-scrub pass, re-verdict is STATUS=GREEN. The legacy hash-less excuse that was added in this section at Bundle 1 has been REMOVED — Bundle 3 patched the gate (v5.16.1) to require hash-locked excuses, which the legacy form does not satisfy.

`limitations-scope-check`: RED → GREEN (RED_HITS=0).

`submission-hygiene`: RED_HITS dropped from 16 → 5. Three hits at L187 are the expected backtick / positional-row / adjudication-log noun triggers inside the new `### Limitations` subsection [ALLOW-PIPELINE-META: forensic correction prose deliberately preserved here per back-route mandate]. Two residual hits at L29 (Introduction) and L97 (Methods) reference pre-registered-families enumeration ("seventeen specifications, seven of which are focal") and the analysis registry / adjudication log — pre-existing pipeline-meta noise that pre-dates this back-route and is out of scope for the H3-scope-relocation pass.

## 附录 G —— `verify-numerics` 报告（完整）

*文件：`output/digital-divide-china-cfps/` `verify/verify-numerics-2026-05-04.md`。Stage-1 数值审计：每条数字主张对锁定 CSV。判决：NEEDS-REVISION（1 WARN——Oaxaca 总差距 0.82 → 0.81）。*

SCANNED: 1 manuscript draft, 4 raw output CSV files (y2-focal-hukou.csv, y1-focal-hukou.csv, oaxaca-decomp.csv, intersection-cells.csv)

###  VERIFICATION REPORT: RAW OUTPUT → MANUSCRIPT CONSISTENCY (STAGE 1)

Manuscript: `output/digital-divide-china-cfps/` `drafts/` `draft-manuscript-digital-divide-china-cfps-2026-05-04.md`
Locked snapshot: `output/digital-divide-china-cfps/results-locked/2026-05-04-1722/tables/`
Date: 2026-05-04

═══════════════════════════════════════════════════════════════════════════

#### SUMMARY

- Manuscript narrative tables (in-prose) audited: 4 (Table 1 Y1 ladder, Table 2 Y2 ladder, Table 3 Oaxaca, Table 4 intersection cells)
- Raw output files matched: 4 of 4
- Numeric claims compared (focal set explicitly named by dispatcher): 21
- Numeric claims verified correct: 19
- Discrepancies (CRITICAL): 0
- Discrepancies (WARNING): 1 (last-decimal rounding on Oaxaca total gap)
- Untraceable values within Stage 1 scope (file not in passed-in set): see UNTRACEABLE block below

#### RAW-TO-MANUSCRIPT MAPPING

| Manuscript object | Source file | Status |
|---|---|---|
| Y2 M1/M2/M3/R1/R2/R4/R5 hukou coefficients (Table 2 ladder + robustness prose) | `tables/y2-focal-hukou.csv` | MATCHED |
| Y1 M1/M2/M3/M4/M5 hukou coefficients (Table 1 ladder + within-person FE prose) | `tables/y1-focal-hukou.csv` | MATCHED |
| Threefold Oaxaca decomposition (Table 3, Figure 5 prose) | `tables/oaxaca-decomp.csv` | MATCHED |
| 8 intersection cell means + n (Table 4, Methods sample-disclosure paragraph) | `tables/intersection-cells.csv` | MATCHED |
| Triple-interaction term (rural × female × pre1965): β = -0.13, SE 1.28, p = 0.92 | not in dispatcher-supplied CSVs | UNTRACEABLE-STAGE1 |
| Cohort gradients on Y2 (3.6, 4.4, 4.1, 1.6, 4.5) | not in dispatcher-supplied CSVs | UNTRACEABLE-STAGE1 |
| Tobit cross-check β = -1.31, SE 0.144 | not in dispatcher-supplied CSVs | UNTRACEABLE-STAGE1 |
| Co-resident young-adult coefficients (+0.59, +1.07) | not in dispatcher-supplied CSVs | UNTRACEABLE-STAGE1 |
| Wave-trajectory endpoints (Y1 -1.0→-0.6; Y2 -1.0 to -1.5) | not in dispatcher-supplied CSVs | UNTRACEABLE-STAGE1 |
| Conditional means (11.9 hrs in 2014; 14.7 in 2018; rural 12.7 vs urban 14.5) | not in dispatcher-supplied CSVs | UNTRACEABLE-STAGE1 |
| N = 204,418 / 54,825 unique pids | declared as `[design:]` in manuscript; no sample-CSV in snapshot | DERIVED-UNVERIFIED → PASS |

#### CELL-BY-CELL COMPARISON

####### Y2 hukou ladder (`y2-focal-hukou.csv` → manuscript Table 2 / Results §H1 / Conclusion)

| Spec | Raw β | Raw SE | Manuscript β | Manuscript SE | Match |
|---|---|---|---|---|---|
| M1 | -2.2317509 | 0.2474814 | -2.23 | 0.247 | YES |
| M2 | -1.6534264 | 0.2846860 | -1.65 | 0.285 | YES |
| M3 (FOCAL) | -1.3059852 | 0.2945688 | -1.31 | 0.295 | YES |
| R1 | NA (collinear) | NA | flagged "missing by design" | — | YES |
| R2 (IPW×design) | -1.3059852 | 0.2945688 | -1.31 ("identical to M3 to three decimal places") | — | YES (raw -1.306 = -1.306) |
| R4 (Deaton-Paxson) | -1.6534264 | 0.2846860 | -1.65 ("identical to M2") | — | YES |
| R5 (3-way interact main) | -0.8935233 | 0.4033632 | -0.89 (lower bound of stated range) | — | YES |

Inferential cross-checks:
- t = -1.30599 / 0.29457 = -4.4337 → manuscript reports t = -4.43. **MATCH.**
- Manuscript reports raw p = 9.27e-6 and BH-FDR p = 1.39e-5. Two-sided p from |t|=4.434 with cluster-robust SE → ≈ 9.3e-6. **CONSISTENT** with raw t (full p-value file not in dispatcher set; treated as derived from coefficient/SE pair).
- BH-FDR p = 1.39e-5 (dispatcher-confirmed focal value). **MATCH** to manuscript abstract, Results, and Conclusion.

####### Y1 hukou ladder (`y1-focal-hukou.csv` → manuscript Table 1 / Results §H1)

| Spec | Raw β | Raw SE | Manuscript β | Manuscript SE | Match |
|---|---|---|---|---|---|
| M1 | -1.7083505 | 0.0361908 | -1.71 | 0.036 | YES |
| M2 | -0.9101322 | 0.0475890 | -0.91 | 0.048 | YES |
| M3 (FOCAL) | -0.8454936 | 0.0511247 | -0.85 | 0.051 | YES |
| M4 (within-person FE) | -0.7236130 | 0.0768367 | -0.72 | 0.077 | YES |
| M5 (stable-core 2014+) | -0.8454936 | 0.0511247 | -0.85 ("matches M3 exactly") | — | YES |

####### Threefold Oaxaca decomposition (`oaxaca-decomp.csv` → manuscript Results §Oaxaca, Conclusion)

| Component | Raw estimate | Raw share | Manuscript estimate | Manuscript share | Match |
|---|---|---|---|---|---|
| Endowments | -0.3952912 | -48.53% | -0.40 | -49% | YES |
| Coefficients | +1.1508496 | +141.29% | +1.15 | +141% | YES |
| Interaction | +0.0589680 | +7.24% | +0.06 | +7% | YES |
| Total gap | 0.8145265 | 100% | "+0.82 hours per week" | — | **WARN** (rounding) |

WARN-RAW-001: Oaxaca total gap is 0.8145 in raw CSV. Standard rounding to two decimals → 0.81, not 0.82. Manuscript reports 0.82 in Results §Oaxaca and embeds it in the share-of-gap arithmetic. The component shares the manuscript reports (-49 / +141 / +7) are computed from the raw 0.8145 denominator (matching the raw `share_of_gap` column to the percent), so the substance is correct; only the standalone "0.82" digit is rounded one tick high. Severity: WARNING (last-decimal rounding; does not flip sign or magnitude order).

####### Intersection cells (`intersection-cells.csv` → manuscript Results §H3 + Methods sample disclosure)

| Cell (rural,female,pre1965) | Raw n | Raw mean_y2 | Manuscript value(s) | Match |
|---|---|---|---|---|
| (0,0,0) urban male <1965-not | 5,315 | 13.447 | n=5,315 (Methods); not separately cited as mean | YES |
| (0,0,1) urban male pre1965 | 1,582 | 11.177 | n=1,582; "urban pre-1965 men 11.2 hours" | YES |
| (0,1,0) urban female <1965-not | 5,266 | 13.150 | n=5,266 | YES |
| (0,1,1) urban female pre1965 | 1,212 | 10.894 | n=1,212; "urban pre-1965 women 10.9 hours" | YES |
| (1,0,0) rural male <1965-not | 11,425 | 12.224 | n=11,425 | YES |
| (1,0,1) rural male pre1965 | 917 | 8.028 | n=917; "rural pre-1965 men 8.0 hours" | YES |
| (1,1,0) rural female <1965-not | 10,672 | 12.412 | n=10,672 | YES |
| (1,1,1) rural female pre1965 | 581 | 7.604 | n=581; "rural pre-1965 women average 7.6 hours" | YES |

Cell-n total = 36,970 → manuscript "Y2 spec ladder uses 36,970 in M2/M3". **CONSISTENT** (DERIVED-VERIFIED).

####### Sample-size design assertions

| Quantity | Raw source | Manuscript | Match |
|---|---|---|---|
| 204,418 person-waves | not in supplied CSVs (declared design figure) | "204,418 person-waves" (abstract, Methods) | DERIVED-UNVERIFIED → PASS |
| 54,825 unique pids | not in supplied CSVs (declared design figure) | "54,825 [design: 54,825]" | DERIVED-UNVERIFIED → PASS (manuscript self-flags as design) |
| Y2 observed waves 2014-2018 | implicit in intersection-cells.csv structure (cells aggregate the Y2 sub-panel) and consistent with manuscript Methods discussion of `qu250m`/`ku250m` items | repeatedly stated | PASS |

#### DISCREPANCIES

####### CRITICAL
None.

####### WARNING
1. **[WARN-RAW-001]** Oaxaca total-gap headline value
   - Raw `oaxaca-decomp.csv` total_gap column = 0.8145265
   - Manuscript Results §Oaxaca: "+0.82 hours per week"; Abstract: "(total = 0.82 hours/week)"
   - Standard half-up rounding of 0.8145 → 0.81 (the digit after the second decimal is 4)
   - Severity: WARNING. Component values, shares, and substantive conclusion unaffected.
   - Suggested fix: replace "0.82" with "0.81" in three locations (abstract, Results §Oaxaca total, Conclusion paragraph if it surfaces) — or report to three decimals (0.815) for transparency.

#### UNTRACEABLE WITHIN STAGE 1 SCOPE

The following manuscript numerics could not be re-traced against the dispatcher-supplied four CSVs. They may exist elsewhere in the locked snapshot (e.g., supplementary tables for cohort gradients, Tobit, FE age slope, wave-interaction). Stage 2 (or a wider snapshot pass) is required to clear them:

- Triple-interaction term (rural × female × pre1965): β = -0.13, SE = 1.28, p = 0.92 (Results §H3, Discussion, Conclusion, Abstract)
- Tobit MLE cross-check: β = -1.31, SE = 0.144 (Results §H1)
- Cohort-gradient point estimates on Y2: -3.6, -4.4, -4.1, -1.6, -4.5 (Results §H2)
- Within-person age slope ≈ -1.0 hours/year (Results §H2)
- Co-resident young-adult coefficients: +0.59 (SE 0.305) and +1.07 (SE 0.634) (Results §H4)
- Wave-trajectory endpoints: Y1 -1.0 (2010) → -0.6 (2020); Y2 range -1.0 to -1.5 across 2014-2018 (Figure 3 prose)
- Conditional-on-user means: 11.9 hrs (2014), 14.7 hrs (2018); rural 12.7 vs urban 14.5 (Figure 1 / Table 1 prose)
- Descriptive composition: rural 4.6 yrs older, 3.1 fewer years schooling (Table 1 prose)

Recommend the orchestrator either widen the dispatcher's CSV list (e.g., `r5-three-way-interaction.csv`, `tobit-y2.csv`, `cohort-gradients.csv`, `wave-interaction.csv`, `descriptives-by-hukou.csv`) or accept these as Stage 1 scope-deferred and route them to Stage 2.

#### CITATION-MARKER NOTE (out-of-scope but flagged)

The manuscript marks every focal numeric with `[CITATION NEEDED]`. This is the Phase 8 references-resolution placeholder, not a numeric-verification gap. Stage 1 numeric audit treats `[CITATION NEEDED]` as cosmetic.

═══════════════════════════════════════════════════════════════════════════

#### SEVERITY-TAGGED ISSUE LIST

- [CRIT] none
- [WARN-RAW-001] Oaxaca total gap reported as 0.82 in manuscript; raw value rounds to 0.81. Last-decimal rounding error; substance unaffected.
- [INFO] 8 numeric claims flagged UNTRACEABLE-STAGE1 because their source CSVs were not in the dispatcher-supplied set. Not a discrepancy; a coverage gap in this Stage 1 pass.

#### VERDICT

**NEEDS-REVISION** — single WARNING-level rounding fix on the Oaxaca total gap (replace "0.82" → "0.81" in abstract, Results §Oaxaca, and any downstream sentence that surfaces the headline gap value). All other focal coefficients (-1.31 / 0.295 / 1.39e-5; -0.85; +1.15 / -0.40 / +0.06; eight intersection cells; 36,970 Y2 sample) match the locked snapshot exactly to the manuscript's reported precision. No critical discrepancies. Eight Stage-1-untraceable claims should be cleared in Stage 2 once a wider snapshot file list is available.

## 附录 H —— `verify-figures` 报告（完整）

*文件：`output/digital-divide-china-cfps/` `verify/verify-figures-2026-05-04.md`。Stage-1 图形审计（含视觉读图）。判决：NEEDS-REVISION（4 CRIT, 2 WARN）：Fig 1 波次覆盖、Fig 2 样本窗口、Fig 3 图形类型、Fig 4 cohort×hukou 模式四处错误。*

SCANNED: 6 manuscript figures, 6 raw figure files

###  VERIFICATION REPORT: RAW OUTPUT → MANUSCRIPT FIGURE CONSISTENCY (STAGE 1)

Manuscript: `output/digital-divide-china-cfps/` `drafts/` `draft-manuscript-digital-divide-china-cfps-2026-05-04.md`
Locked figures: `output/digital-divide-china-cfps/results-locked/2026-05-04-1722/figures/`
Date: 2026-05-04

═══════════════════════════════════════════════════════════════════════════

#### SUMMARY

- Figure files found: 6 (fig1-fig6, all PDF)
- Figure references in manuscript: 6 (Figure 1, 2, 3, 4, 5, 6)
- Figures verified consistent with raw data: 1 (Fig 6)
- Figures with partial / borderline match: 1 (Fig 5)
- Figures with CRITICAL discrepancies: 4 (Figs 1, 2, 3, 4)
- Missing figures (referenced but no file): 0
- Orphaned figures (file exists, no reference): 0

#### FIGURE INVENTORY

| Figure | File Path (relative to results-locked/2026-05-04-1722/) | Sidecar Data | Referenced? |
|--------|----------------------------------------------------------|--------------|-------------|
| Fig 1  | figures/fig1-access-trend.pdf | fig1-access-trend-data.csv | YES |
| Fig 2  | figures/fig2-Y2-by-cohort.pdf | (none found) | YES |
| Fig 3  | figures/fig3-hukou-coef-trajectory.pdf | (none found) | YES |
| Fig 4  | figures/fig4-Y2-by-hukou-cohort.pdf | (none found) | YES |
| Fig 5  | figures/fig5-oaxaca-decomp.pdf | (none found) | YES |
| Fig 6  | figures/fig6-intersection-cells.pdf | (none found) | YES |

#### VISUAL INSPECTION SUMMARY (VLM)

| Figure | Axes | Legend | Color | Data-Ink | Panels | Truncation | Resolution | Overall |
|--------|------|--------|-------|----------|--------|------------|------------|---------|
| Fig 1  | PASS | PASS | PASS | PASS | N/A | PASS | PASS | GOOD |
| Fig 2  | PASS | N/A  | PASS | PASS | N/A | PASS | PASS | GOOD |
| Fig 3  | PASS | N/A  | PASS | PASS | N/A | PASS | PASS | GOOD |
| Fig 4  | ISSUE (x-axis tick labels overlap "Birth cohort" axis title) | PASS | PASS | PASS | N/A | PASS | PASS | ACCEPTABLE |
| Fig 5  | PASS | N/A  | PASS | PASS | N/A | PASS | PASS | GOOD |
| Fig 6  | PASS | PASS | PASS | PASS | N/A | PASS | PASS | GOOD |

VLM-DETECTED ISSUES:
1. [VLM-FIG-001] Figure 4 — long cohort tick labels (`<=1955`, `1956−1965`, ...) overlap the axis title "Birth cohort". Same minor overlap visible in Figure 2. WARNING (cosmetic).

#### CAPTION-VISUAL MATCH (substantive)

####### Figure 1 — `fig1-access-trend.pdf`
- **Caption claim**: "Internet access by hukou, 2010–2020"; "Design-weighted shares; CFPS adult sample (age 16+)" → Image shows two lines (Rural / Urban), x-axis 2010–2020 → MATCH on title, but x-axis only contains points at 2010, 2014, 2018, 2020 (no 2012, no 2016).
- **In-text claim** (line 113): "rose from approximately 24 percent in 2010 to approximately 67 percent in 2020" → Image shows rural≈20%, urban≈47% in 2010, rural≈60%, urban≈79% in 2020. The pooled-mean trajectory is not directly plotted, but the per-group endpoints are visible and consistent with the underlying CSV.
- **In-text claim** (line 113): "rural-urban gap closed from roughly 40 percentage points in 2010 to roughly 15 percentage points in 2020" → CSV gives 2010 gap = 47.32 − 20.20 = **27.1 pp**, not 40 pp; 2020 gap = 78.98 − 60.28 = **18.7 pp**, not 15 pp. **MISMATCH.**
- **In-text claim** (line 99): "the access-trend figure shows a smooth trajectory across the six waves" → Figure plots only **four** waves (2010, 2014, 2018, 2020). The 2012 and 2016 waves are missing. **MISMATCH.**
- **Overall**: PARTIAL → contains a CRITICAL numeric mismatch on the "40 pp" claim and a CRITICAL coverage mismatch ("six waves" vs. four plotted).

####### Figure 2 — `fig2-Y2-by-cohort.pdf`
- **Caption claim**: "Distribution of Y2 weekly internet hours by cohort"; "CFPS 2014–2020 users (Y1=1); n = 41,621" → Image is a violin+boxplot panel by six cohort bands. Title and content match.
- **In-text claim** (line 133): "Figure 2 plots the implied cohort trajectories" → The figure does **not** plot trajectories (lines/curves over cohort with point estimates); it plots **distributions** (violins+boxes). MISMATCH on form.
- **Sample-window claim**: figure subtitle says "CFPS 2014–**2020** users". Manuscript Methods (line 99) and Results (line 87, 113) restrict Y2 to **2014–2018** because the 2020 module reorganization is non-comparable. The figure includes wave 2020 in Y2; the manuscript explicitly excludes it. **MISMATCH** between figure data window and the manuscript's stated Y2 scope.
- **n claim**: figure says n = 41,621; manuscript line 87 reports Y2 analytic file = 40,913 person-waves (and 36,970 in M2/M3 after listwise deletion). The 41,621 in the figure does not correspond to the 40,913 manuscript figure for the 2014–2018 panel; it likely reflects the 2014–**2020** inclusion. **MISMATCH.**
- **Overall**: MISMATCH (form: distributions vs. trajectories; window: 2014–2020 vs. 2014–2018; n disagreement).

####### Figure 3 — `fig3-hukou-coef-trajectory.pdf`
- **Caption claim** (figure title): "Hukou access gap, 2010–2020"; subtitle "Design-weighted difference in P(any internet use)"; y-axis "Urban-rural Y1 access gap (percentage points)" → Image is a **bar chart of percentage-point access gaps** by wave. Bars at 2014=21, 2016=12, 2018=21, 2020=19.
- **In-text claim** (line 121, 123, 151): "wave-interacted Y1 variant (Figure 3) shows the rural-hukou **logit coefficient** narrowing across waves: from approximately minus 1.0 in 2010 to approximately minus 0.6 in 2020"; "auxiliary tests of the H1 wave-trajectory claim (Figure 3) plot the rural-hukou coefficient against wave for both Y1 and Y2". → The figure plots **descriptive percentage-point gaps**, not regression-coefficient trajectories, and shows **only Y1**, not "both Y1 and Y2". The figure's 2014→2020 sequence (21, 12, 21, 19 pp) is **not monotonically narrowing**. **CRITICAL MISMATCH.**
- **Year coverage**: title says "2010–2020" but x-axis is **2014, 2016, 2018, 2020** (no 2010, 2012). **MISMATCH** between figure title and figure content.
- **Overall**: MISMATCH on figure type (descriptive bars vs. coefficient trajectory), on outcome scope (only Y1 vs. both), on direction claim (not monotonic), and on year coverage (2014–2020 vs. claimed 2010–2020).

####### Figure 4 — `fig4-Y2-by-hukou-cohort.pdf`
- **Caption claim**: "Use intensity by hukou and cohort"; subtitle "Y1=1 sample, design-weighted; CI is 95%" → Two lines (Rural, Urban) by 6 cohort bands with 95% CIs. Form matches.
- **In-text claim** (line 147): "at every cohort, the rural curve sits below the urban curve" → Image shows rural below urban for cohorts ≤1955 through 1986–1995, but for cohort **1996+ the two curves converge** (rural ≈ urban ≈ 13.5 hours, urban actually slightly below or equal). **MISMATCH** — "every cohort" is not literally true.
- **In-text claim** (line 147): "the vertical distance between the curves does not narrow across cohorts in the way a 'young rural cohorts catch up' hypothesis would predict" → Visually the gap **does** narrow noticeably between 1986–1995 and 1996+ (almost closes). The figure visually supports the catch-up hypothesis at the youngest cohort. **MISMATCH.**
- **In-text claim** (line 153): "Among the youngest observed cohort (1996+) the rural-urban gap is in fact larger than among the oldest cohorts" → Image shows the 1996+ gap is **smaller** (essentially zero) than the ≤1955 gap (≈ 5 hours). **CRITICAL MISMATCH** — opposite direction to what figure shows.
- **Overall**: MISMATCH on three substantive claims about the cohort × hukou pattern.

####### Figure 5 — `fig5-oaxaca-decomp.pdf`
- **Caption claim**: "Threefold Oaxaca-Blinder decomposition of Y2"; subtitle "Total gap = **0.81** hours/week"; y-axis "Hours/week (rural − urban)" → Bars: Endowments ≈ −0.40 (with CI to −0.6), Coefficients ≈ +1.15 (CI 0.83–1.48), Interaction ≈ +0.06 (CI −0.22 to +0.33).
- **In-text claim** (line 129): "The total rural-urban Y2 gap implied by the decomposition is **+0.82** hours per week" → Figure subtitle reports 0.81. Minor rounding mismatch (0.81 vs. 0.82). WARNING.
- **In-text claim** (line 15, 129, 181): "endowments component is minus 0.40 hours" / "coefficients (returns) component is +1.15 hours" / "interaction is +0.06 hours" → MATCH.
- **Sign convention note**: y-axis label is "Hours/week (rural − urban)" but text (line 129) says "+0.82 hours per week (urban higher; the sign of the gap is set by the package convention with the rural group as reference)". The signs on the bars in the figure (negative endowments, positive coefficients, positive total) are internally consistent with the package's "rural is the reference, computed gap is urban − rural" convention even though the y-axis label literally says the opposite. **WARNING** — the y-axis label "(rural − urban)" appears reversed relative to the underlying convention; the manuscript description is correct, but a reader will be confused by the axis label.
- **Overall**: MATCH on component magnitudes; WARNING on (a) total-gap rounding (0.81 vs. 0.82) and (b) potentially mislabeled y-axis sign convention.

####### Figure 6 — `fig6-intersection-cells.pdf`
- **Caption claim**: "Intersectional cell means: Y2 use intensity"; subtitle "Rural × female × pre-1965 cohort cells" → Image is a horizontal bar chart with 8 cells, color-coded by pre-/post-1965 cohort.
- **In-text claim** (line 139): "rural pre-1965 women average 7.6 hours of weekly use, rural pre-1965 men 8.0 hours, urban pre-1965 women 10.9 hours, urban pre-1965 men 11.2 hours" → Figure bars (read visually): Rural Female ≤1965 ≈ 7.5, Rural Male ≤1965 ≈ 8, Urban Female ≤1965 ≈ 10.9, Urban Male ≤1965 ≈ 11. **MATCH** to one decimal.
- **In-text claim**: rural pre-1965 women is the lowest cell → Figure: bars sorted; Rural Female ≤1965 is at the bottom (lowest). MATCH.
- **Overall**: MATCH.

#### CAPTION-VISUAL MISMATCHES (CRITICAL)

1. **[CRIT-FIG-VSM-001] Figure 1 — wave coverage and gap magnitudes.** Manuscript Methods says the access-trend figure shows a "smooth trajectory across the six waves" (line 99) and Results states the rural-urban gap closed "from roughly 40 percentage points in 2010 to roughly 15 percentage points in 2020" (line 113). Figure plots **four** waves (2010, 2014, 2018, 2020), not six, and the underlying CSV gives a 2010 gap of **27.1 pp** (not 40) and a 2020 gap of **18.7 pp** (not 15). Either the figure must be regenerated to include 2012 and 2016, or the manuscript narrative must be revised to reflect the actual gap magnitudes.

2. **[CRIT-FIG-VSM-002] Figure 2 — sample window and figure form.** Figure 2 subtitle says "CFPS 2014–**2020** users (Y1=1); n = 41,621" but the manuscript repeatedly restricts Y2 to **2014–2018** (Methods line 87, line 99: "we therefore restrict Y2 analyses to the three waves with comparable items, yielding an analytic sample of 40,913 person-waves"). Including 2020 in the figure contradicts the headline scope claim. Separately, the manuscript text describes Figure 2 as plotting "the implied cohort trajectories" (line 133), but the figure renders **distribution violins+boxes**, not trajectories.

3. **[CRIT-FIG-VSM-003] Figure 3 — figure type and outcome do not match the cited claim.** Manuscript references Figure 3 as plotting "the rural-hukou logit coefficient" against wave with values narrowing from ≈ −1.0 in 2010 to ≈ −0.6 in 2020 (lines 121, 123, 151), and as plotting "both Y1 and Y2" (line 151). The actual figure is a **bar chart of descriptive percentage-point access gaps for Y1 only** (no Y2 panel, no logit coefficients), the bars are not monotonically narrowing (21, 12, 21, 19 across 2014/2016/2018/2020), and the figure does not include 2010 or 2012 despite a title that says "2010–2020". This is a wholesale figure-type mismatch and is the most consequential discrepancy in the report.

4. **[CRIT-FIG-VSM-004] Figure 4 — three substantive cohort-pattern claims contradicted by the image.**
   - Manuscript line 147 says "at every cohort, the rural curve sits below the urban curve"; Figure shows rural ≈ urban (or rural slightly above urban) at the 1996+ cohort.
   - Manuscript line 147 says the vertical gap "does not narrow across cohorts"; Figure shows visible narrowing between 1986–1995 and 1996+.
   - Manuscript line 153 says "Among the youngest observed cohort (1996+) the rural-urban gap is in fact larger than among the oldest cohorts"; Figure shows the 1996+ gap is **smaller** (effectively zero) than the ≤1955 gap (≈ 5 hours). This claim runs in the opposite direction of the data plotted.

#### WARNINGS

1. **[WARN-FIG-001] Figure 5 — total-gap rounding.** Figure subtitle reports total gap = 0.81 hours/week; manuscript text reports +0.82. Likely a rounding/recompute mismatch; reconcile to a single value.
2. **[WARN-FIG-002] Figure 5 — y-axis sign-convention label.** Y-axis label "Hours/week (rural − urban)" reads literally opposite to the manuscript's stated sign convention (line 129: "the sign of the gap is set by the package convention with the rural group as reference"). Either flip the bar signs or re-label the axis "Hours/week (urban − rural)".
3. **[WARN-FIG-003] Figures 2 and 4 — overlapping x-axis tick labels.** Long cohort labels overlap the "Birth cohort" axis title. Cosmetic.
4. **[WARN-FIG-004] Sidecar data CSVs missing for Figures 2–6.** Only Fig 1 has a `*-data.csv` sidecar. Provide sidecars for the remaining figures to enable downstream verification.

#### MISSING FIGURES

None — all six referenced figures have files.

#### ORPHANED FIGURES

None.

#### FIGURE-TABLE CROSS-CHECK

| Figure | Related Table / Manuscript Numbers | Values Match? | Notes |
|--------|-----------------------------------|---------------|-------|
| Fig 1 (access trend) | Table 1; manuscript abstract figures (24% → 67%) | PARTIAL | Per-group rural/urban shares from CSV consistent with figure; aggregated 24%/67% claim and 40 pp / 15 pp gap claim do **not** reconcile with CSV. |
| Fig 2 (Y2 cohort distribution) | Table 4; manuscript line 133 cohort gradients | UNVERIFIABLE | Figure shows distributions only; manuscript reports M3 cohort coefficients (-3.6, -4.4, -4.1, -1.6, -4.5) which are not visually represented. Figure window (2014–2020) inconsistent with Y2 scope (2014–2018). |
| Fig 3 (claimed coef trajectory) | Table 1 wave-interacted Y1 panel | NO | Figure plots descriptive pp gaps, not logit coefficients; not narrowing as claimed. |
| Fig 4 (Y2 hukou × cohort means) | Table 4 / line 153 | PARTIAL | Visual pattern at oldest cohorts roughly consistent; pattern at 1996+ contradicts manuscript narrative. |
| Fig 5 (Oaxaca decomp) | Table 3 oaxaca-decomp | YES (with WARN) | Components match (-0.40, +1.15, +0.06); total 0.81 vs. 0.82 minor; sign-convention label confusing. |
| Fig 6 (intersection cells) | Table 4 | YES | Cell means match manuscript (7.6, 8.0, 10.9, 11.2). |

═══════════════════════════════════════════════════════════════════════════

#### VERDICT

**NEEDS-REVISION**

Four CRITICAL caption-visual mismatches (Figs 1, 2, 3, 4) plus two WARNINGs on Fig 5. The most consequential issue is **Figure 3**, which the manuscript repeatedly cites as a wave-by-wave coefficient trajectory plot for both Y1 and Y2, but which is in fact a bar chart of descriptive Y1 access-gap percentages over a partial year window — a figure-type, outcome-scope, and direction-of-effect mismatch in one. **Figure 4** carries three contradicted cohort-pattern claims that materially affect the institutional-sorting reading at the youngest cohort. **Figure 1** has both numeric (gap magnitudes) and coverage (4 waves vs. claimed 6) discrepancies. **Figure 2** is plotted on a 2014–2020 window that contradicts the manuscript's stated 2014–2018 Y2 scope.

Recommended next steps before figure-lock:
1. Regenerate Figure 3 as the wave-by-wave hukou coefficient trajectory (Y1 and Y2 panels) the manuscript actually describes, or revise the prose to describe the descriptive bar chart that exists.
2. Reconcile Figure 1's wave coverage (add 2012, 2016) and reconcile the "40 pp / 15 pp" / "24% / 67%" narrative against the CSV.
3. Decide on the Y2 sample window (2014–2018 vs. 2014–2020) and apply the choice consistently across Methods, Figures 2 and 4, and the n reported in the figure subtitles.
4. Rewrite the Figure 4 narrative around the visible pattern (or regenerate the figure if the data should show a non-narrowing gap at 1996+).
5. Reconcile Figure 5's total-gap value (0.81 vs. 0.82) and either flip bar signs or re-label the y-axis.
6. Add `*-data.csv` sidecars for Figures 2–6 to enable downstream value-level checks.

WROTE: /Users/yongjunzhang/Library/CloudStorage/GoogleDrive-joshzyj@gmail.com/My Drive/Claude-Code-Skill/workshop/cfps-example/output/digital-divide-china-cfps/verify/verify-figures-2026-05-04.md

## 附录 I —— `verify-logic` 报告（完整）

*文件：`output/digital-divide-china-cfps/` `verify/verify-logic-2026-05-04.md`。Stage-2 逻辑审计：每条方向 / 显著性主张对表中正确行。判决：NEEDS-REVISION（2 CRIT, 5 WARN）。H3 取错行 CRIT 是工作坊最有教学意义的失败案例。*

SCANNED: 7 manuscript sections (Abstract, Introduction, Theoretical Framework, Data and Methods, Results, Discussion, Conclusion); 6 in-prose tables/figures cited (Table 1, Table 2, Table 3, Table 4, Figure 1–6).

VERIFICATION REPORT: MANUSCRIPT TABLE/FIGURE → PROSE CONSISTENCY (STAGE 2)

════════════════════════════════════════════════════════════════════════════

SUMMARY
- Statistical claims extracted: 41
- Claims verified internally consistent: 36 (88%)
- Discrepancies / external-source flags: 5
- Cross-section contradictions: 1
- Causal language issues: 1

────────────────────────────────────────────────────────────────────────────

CRITICAL DISCREPANCIES

1. [CRIT-TXT-001] Results §H3 (para containing "[Table 4]"); Abstract; Discussion §H3; Conclusion
   - Text states (Results): "The three-way interaction term rural-hukou by female by pre-1965 in specification R5 returns a coefficient of minus 0.13 hours per week with a standard error of 1.28 (p = 0.92)."
   - Text states (Abstract): "The intersectional triple-penalty hypothesis ... is not supported: the three-way interaction is null (p = 0.92)."
   - Text states (Discussion): "H3 is not supported. The three-way rural-by-female-by-pre-1965 interaction is statistically null (p = 0.92)."
   - Text states (Conclusion): "p = 0.92"
   - Source-document evidence (`analysis/limitations-accepted.md`, "Late-caught CRITs," entries CRIT-CORR-005 / CRIT-STAT-003): "scripts/05-decomposition.R lines 125–129 extracted the hukou_rural main-effect coefficient from R5 instead of the hukou_rural:female:pre1965 triple-interaction row. The reported H3 p = 0.92 is therefore the main-effect p, not the three-way-interaction p. Action: fixed in iter2 of the script ... H3 verdict re-derived from the correct row, recorded as H3-CORRECTED in adjudication-log.csv."
   - Problem: The four sections (Abstract, Results, Discussion, Conclusion) all attribute the value `p = 0.92` to the **triple-interaction row** of R5, but per the recorded code-review CRIT, that p-value is the **main-effect** row. The triple-interaction p (the one the H3 hypothesis actually requires) is not reported anywhere in the manuscript prose. The H3-NOT-SUPPORTED verdict may still be correct under the corrected row, but the **prose attributes the wrong row's p-value to the H3 test**, which is a number-mismatch between prose and the evidence the prose claims to be quoting.
   - Fix: (a) Replace `p = 0.92` with the corrected triple-interaction row p-value from `adjudication-log.csv` (`H3-CORRECTED`) in all four locations; (b) re-state the coefficient (currently −0.13) and SE (currently 1.28) from the correct row; (c) re-derive the H3 verdict from the corrected row and update Abstract/\allowbreak{}Results/\allowbreak{}Discussion/\allowbreak{}Conclusion adjudications accordingly.
   - Severity: CRITICAL — same value mis-cited in four sections; affects the central H3 adjudication.

2. [CRIT-TXT-002] Methods §estimator + §robustness — Y2 focal estimator labeling
   - Text states (Methods): "For Y2, the M3 estimator is OLS (linear hours) with the same SE structure and an MLE Tobit cross-check…"
   - Text states (Results): "The Tobit MLE cross-check on the same specification returns minus 1.31 (SE 0.144), confirming the linear-feols magnitude under the alternative likelihood."
   - Source-document evidence (`limitations-accepted.md`, CRIT-STAT-001): "focal Y2.M3 is feols (OLS with FE), not Tobit MLE… the manuscript Methods should describe Y2.M3 as OLS with FE plus a Tobit MLE robustness check."
   - Status: The manuscript Methods text now correctly states M3 is OLS with Tobit as cross-check. The Abstract still says "logit, linear, and Tobit specifications" which is consistent if read as a list of estimators used somewhere in the paper, not as the focal estimator. **Apparent agreement** between Methods statement and corrected interpretation. Not a logic CRIT against current draft, but flagged to confirm Phase 7 fix landed.
   - Severity: RESOLVED in current draft text; verify alignment when reviewing supplementary tables.

────────────────────────────────────────────────────────────────────────────

WARNINGS

1. [WARN-TXT-001] Results §Oaxaca decomposition vs. Results §Table 1 raw gap
   - Text states (Oaxaca para): "The total rural-urban Y2 gap implied by the decomposition is +0.82 hours per week."
   - Text states (Table 1 description, two paragraphs later): "the conditional-on-user weekly-hours mean is 12.7 hours per week (rural) versus 14.5 hours per week (urban), a raw 1.8-hour gap."
   - Issue: The manuscript reports two different "rural-urban Y2 gap" magnitudes (0.82 vs 1.8) without explicitly reconciling that the Oaxaca decomposition operates on a different analytic sub-sample / weighting than the Table 1 descriptive means. A careful reader will compute (1.8 − 1.31)/1.8 ≈ 27% absorbed (text says "approximately 30 percent") which uses 1.8 as the gap, but the abstract claims 0.82 as "total." Both are correct but are not the same quantity.
   - Fix: Add one sentence in the Oaxaca paragraph clarifying: "The Oaxaca total of +0.82 hours differs from the Table 1 raw means difference of 1.8 hours because the decomposition is computed on the M3 estimation sample with covariate-adjusted urban means rather than on raw cell means."
   - Severity: WARNING — both numbers are individually defensible; the reader-facing inconsistency is a presentation issue.

2. [WARN-TXT-002] Results §H4 — "partial support" with p = 0.054
   - Text states: "Co-residence with a digital-native household member ... is associated with +0.59 hours per week ... (SE 0.305; p = 0.054) and +1.07 hours per week in the within-person fixed-effects specification (SE 0.634)."
   - Text states (Discussion): "H4 receives modest support as a secondary mechanism finding."
   - Issue: p = 0.054 with the conventional 0.05 threshold normally would not support a positive verdict. Manuscript's hedge ("partial / modest support") is consistent across Results and Discussion, and the FE coefficient is much larger (+1.07), so the soft framing is defensible — but on the focal cross-sectional spec alone, calling this "support" is generous.
   - Fix: Either tighten language to "marginal" / "borderline" or add an explicit sentence noting that the cross-sectional p exceeds the 0.05 threshold and that the verdict rests jointly on the FE estimate's larger magnitude.
   - Severity: WARNING.

3. [WARN-TXT-003] Results §H2 cohort gradients — "ordered" claim
   - Text states: "the M3 cohort gradients on Y2 are large and ordered as the cohort-as-cause account predicts: relative to the pre-1955 reference cohort, the 1956-1965 band sits 3.6 hours per week lower, 1966-1975 sits 4.4 hours per week lower, 1976-1985 sits 4.1 hours per week lower, 1986-1995 sits 1.6 hours per week lower, and 1996+ sits 4.5 hours per week lower (the apparent reversal at 1996+ is driven by a small in-school subsample…)."
   - Issue: The numerical sequence (−3.6, −4.4, −4.1, −1.6, −4.5) is **not monotonically ordered** in either direction: the gradient becomes *more* negative from 1956-65 to 1966-75 (opposite of cohort-as-cause prediction), recovers between 1966-75 and 1986-95, then plunges again at 1996+. Manuscript flags only the 1996+ reversal as an artifact; the 1956-65 → 1966-75 → 1976-85 non-monotonicity is not addressed. The claim "ordered as the cohort-as-cause account predicts" is therefore overstated.
   - Fix: Soften language to "broadly consistent with cohort gradients" and acknowledge the non-monotonic interior pattern, OR explain that the pre-1955 reference is itself a small/extreme cell that distorts the contrast.
   - Severity: WARNING — non-monotonic pattern is partially explained (1996+) but not fully (interior).

4. [WARN-TXT-004] Discussion / Conclusion magnitude rounding ("approximately 1.3")
   - Text states (Discussion): "agricultural-hukou status reduces weekly internet use among users by approximately 1.3 hours per week."
   - Text states (Results / Abstract): "minus 1.31 hours per week."
   - Issue: Rounding 1.31 → 1.3 is acceptable but technically each rounding compounds when discussed in compounded form ("a 1.31-hour residual ... approximately 30 percent of the raw gap absorbed"). All within tolerance, but worth one consistent decimal-place convention.
   - Fix: Adopt a uniform decimal-place convention across Abstract/\allowbreak{}Results/\allowbreak{}Discussion/\allowbreak{}Conclusion.
   - Severity: WARNING (low).

5. [WARN-TXT-005] Robustness range claim
   - Text states (Results §robustness): "the rural-hukou coefficient on Y2 sits between minus 0.89 and minus 2.23"
   - Issue: The manuscript reports M1 = −2.23, M2 = −1.65, M3 = −1.31, R2 (IPW) = −1.31, R4 (Deaton-Paxson) = −1.65. None of the in-prose specifications gives −0.89; the lower bound of the range is therefore from one of the unreported supplementary specifications (likely R6 stable-core or R5b wave-interacted). The reader cannot verify the −0.89 endpoint from in-prose tables.
   - Fix: Cite the specific spec that yields −0.89 (e.g., "R5b 2018 wave-interacted estimate") so the reader can locate the source.
   - Severity: WARNING.

────────────────────────────────────────────────────────────────────────────

HYPOTHESIS ADJUDICATION TABLE

| Hypothesis | Prediction | Table/Spec | Result in Prose | Manuscript Verdict | Correct given current draft? |
|-----------|-----------|------------|-----------------|--------------------|------------------------------|
| H1 (hukou persistence) | rural − on Y1 (narrowing); rural − on Y2 (stable) | Table 1 (Y1) M3; Table 2 (Y2) M3; Fig 3 wave-interaction | Y1: b=−0.85, BH-FDR p<1e-60; Y2: b=−1.31, BH-FDR p=1.39e-5; Y2 wave-interacted between −1.0 and −1.5 (flat); Y1 narrows ~−1.0 → ~−0.6 | SUPPORTED (both legs) | YES |
| H2 (cohort layering) | sharp cohort gradients; flat within-person age slope | M3 cohort coefs; R1 within-person FE | gradients large but non-monotonic; within-person age slope ≈ 0 | DESCRIPTIVELY SUPPORTED, formally DEFERRED (HAPC variance-share not run) | PARTIALLY — see WARN-TXT-003 on monotonicity |
| H3 (intersectional triple penalty) | rural × female × pre-1965 < 0, larger than additive sum | R5 three-way interaction; Table 4 cells; Fig 6 | b=−0.13, SE=1.28, p=0.92 (but per limitations-accepted, p=0.92 is the **main-effect** row, not the triple-interaction row) | NOT SUPPORTED | INCONCLUSIVE — see CRIT-TXT-001. The p-value cited is from the wrong R5 row; the corrected triple-interaction p (in `adjudication-log.csv` H3-CORRECTED) should replace 0.92 in prose. The verdict (NOT SUPPORTED) may stand under the corrected row but the cited evidence is wrong. |
| H4 (household spillover) | + effect of co-resident young adult on Y1, Y2 | M3 cross-section; FE variant | b=+0.59, p=0.054 (cross-section); b=+1.07 (FE) | PARTIAL / MODEST SUPPORT (secondary) | YES with caveat — see WARN-TXT-002 |

────────────────────────────────────────────────────────────────────────────

CROSS-SECTION CONTRADICTIONS

1. [CONTRA-001] Oaxaca total gap (0.82) vs Table 1 raw gap (1.8)
   - See WARN-TXT-001 above. Same finding described with two different "total gap" numbers in adjacent paragraphs without reconciling them.

(No other contradictions: Abstract numbers (−1.31, −0.85, +1.15, −0.40, p=0.92), Results numbers, Discussion numbers, and Conclusion numbers all match each other. Caveat: all four sections share the H3 row-extraction error documented in CRIT-TXT-001, so the consistency is "consistently wrong-rowed.")

────────────────────────────────────────────────────────────────────────────

CAUSAL LANGUAGE AUDIT

| Location | Text | Design | Appropriate? |
|----------|------|--------|--------------|
| Abstract, Conclusion | "agricultural-hukou status reduces weekly use by 1.31 hours" | Observational logit/OLS with province-by-wave FE; current hukou (not birth hukou); no IV, no discontinuity | BORDERLINE — The Methods explicitly disclaims causal identification ("future research should ... an instrument for hukou ... CFPS does not supply"), and the Discussion frames hukou as institutional sorting rather than a manipulable cause. The verb "reduces" should be replaced with "is associated with X fewer hours" or "predicts X fewer hours" in the Abstract and Conclusion to match the design. |
| Results §Y2 ladder | "rural-hukou coefficient is minus 2.23 hours per week ... indicating that rural-hukou users report on average 2.23 fewer weekly hours" | Same | OK — this phrasing is descriptive ("report on average") |
| Discussion §implications | "the policy lever is *not* simply equalizing access ... it runs through the institutional opportunity structure" | Same | OK — appropriately frames as structural rather than causal |
| Discussion §objection | Acknowledges that "Distinguishing these mechanisms cleanly would require an instrument for hukou or a discontinuity-design exploiting hukou-conversion thresholds, which CFPS does not supply" | Same | EXEMPLARY — explicit disclaimer present |

Single recommendation: replace "reduces" with "is associated with a reduction of" in Abstract and Conclusion to match the explicit causal-design disclaimer in the Discussion.

────────────────────────────────────────────────────────────────────────────

ABSTRACT ACCURACY

| Abstract Claim | Source in Manuscript | Verified? | Notes |
|----------------|----------------------|-----------|-------|
| "N = 204,418 person-waves; 54,825 unique respondents" | Methods §sample | YES | Matches |
| "Y2 rural-hukou coef = −1.31 (SE 0.295; BH-FDR p = 1.39e-5)" | Results Table 2 M3 | YES | Internally matches Results |
| "Y1 rural-hukou logit coef = −0.85 (BH-FDR p < 1e-60)" | Results Table 1 M3 | YES | Matches |
| "Total Oaxaca gap = 0.82 hours/week" | Results Oaxaca para | YES | Matches; differs from raw 1.8-hour gap (see WARN-TXT-001) |
| "Coefficients component = +1.15 hours" | Results Table 3 | YES | Matches; +141% of 0.82 ≈ correct |
| "Endowments component = −0.40 hours" | Results Table 3 | YES | Matches; −49% of 0.82 ≈ correct |
| "H3 three-way interaction is null (p = 0.92)" | Results §H3 | NO — see CRIT-TXT-001 | The 0.92 is the main-effect-row p in R5, not the triple-interaction-row p; the actual three-way-interaction p is recorded in `adjudication-log.csv` H3-CORRECTED row |

────────────────────────────────────────────────────────────────────────────

CLAIM VERIFICATION LOG (representative)

| # | Claim (abbreviated) | Source spec | Prose value | Match across sections? |
|---|---------------------|-------------|-------------|------------------------|
| 1 | Y2 M3 rural coef = −1.31 | T2 M3 | −1.31 (Abstract, Results, Discussion, Conclusion) | YES |
| 2 | Y2 M3 SE = 0.295 | T2 M3 | 0.295 (Abstract, Results) | YES |
| 3 | Y2 M3 BH-FDR p = 1.39e-5 | T2 M3 | 1.39e-5 (Abstract, Results, Conclusion) | YES |
| 4 | Y2 M1 rural coef = −2.23 | T2 M1 | −2.23 (Results) | YES |
| 5 | Y2 M2 rural coef = −1.65 | T2 M2 | −1.65 (Results) | YES |
| 6 | Tobit MLE Y2 coef = −1.31 (SE 0.144) | Robustness | −1.31 / 0.144 (Results) | YES |
| 7 | Y1 M3 rural coef = −0.85 | T1 M3 | −0.85 (Abstract, Results, Discussion, Conclusion) | YES |
| 8 | Y1 M3 SE = 0.051 | T1 M3 | 0.051 (Results) | YES |
| 9 | Y1 M1 rural coef = −1.71 | T1 M1 | −1.71 (Results) | YES |
| 10 | Y1 within-person FE coef = −0.72 (SE 0.077) | R1 | −0.72 / 0.077 (Results, robustness) | YES |
| 11 | Oaxaca total = +0.82 | T3 | +0.82 (Abstract, Results) | YES |
| 12 | Oaxaca endowments = −0.40 (−49%) | T3 | −0.40 / −49% (Abstract, Results, Conclusion) | YES |
| 13 | Oaxaca coefficients = +1.15 (+141%) | T3 | +1.15 / +141% (Abstract, Results, Conclusion) | YES |
| 14 | Oaxaca interaction = +0.06 (+7%) | T3 | +0.06 / +7% (Results) | YES |
| 15 | H3 three-way: b=−0.13, SE=1.28, p=0.92 | R5 | reported across 4 sections | NO — wrong R5 row per limitations-accepted CRIT-CORR-005 / CRIT-STAT-003 |
| 16 | H4 cross-section coef = +0.59, p=0.054 | M3 H4 | +0.59 / 0.054 (Results) | YES |
| 17 | H4 FE coef = +1.07, SE=0.634 | R1 H4 | +1.07 / 0.634 (Results) | YES |
| 18 | Y2 2014 mean = 11.9; 2018 mean = 14.7 | T1 wave means | 11.9, 14.7 (Abstract, Results) | YES |
| 19 | Y2 rural mean 2014-18 = 12.7; urban = 14.5 | T1 hukou means | 12.7, 14.5 (Results) | YES |
| 20 | Raw rural-urban Y2 gap = 1.8 hrs | derived | 1.8 (Results) | YES (but differs from Oaxaca total 0.82 — see CONTRA-001) |
| 21 | "30% absorbed by M3 / 70% persists" | derived (1.31/1.8) | matches arithmetic 27%/73% ≈ 30%/70% | YES |
| 22 | Cohort gradient 1956-65 = −3.6 | T2 M3 cohort coefs | −3.6 (Results) | YES |
| 23 | Cohort gradients ordered as predicted | claim | non-monotonic interior | NO — see WARN-TXT-003 |
| 24 | Y1 2010 wave-interacted ≈ −1.0; 2020 ≈ −0.6 | Fig 3 / R5b | −1.0 / −0.6 (Results, Discussion) | YES |
| 25 | Y2 wave-interacted between −1.0 and −1.5 (flat) | R5b | −1.0 to −1.5 (Results, Discussion) | YES |
| 26 | Robustness Y2 range: −0.89 to −2.23 | unspecified | endpoints don't both appear in prose | PARTIAL — see WARN-TXT-005 |
| 27 | Y1 robustness range: −0.72 to −1.71 | various | both endpoints traceable | YES |
| 28 | Stable-core 2014+ M5 Y1 coef = −0.85 | M5 | −0.85 (Results) | YES (matches M3) |
| 29 | Deaton-Paxson R4 Y2 coef = −1.65 | R4 | −1.65 (Results) | YES (matches M2) |
| 30 | IPW R2 Y2 coef = −1.31 | R2 | −1.31 (Results) | YES (matches M3) |
| 31 | Hukou conversion < 2% of person-waves | Methods | < 2% | YES (used twice consistently) |
| 32 | Sample 119,259 rural / 35,762 urban / 49,397 missing | Methods | YES | YES |
| 33 | Wave-level Ns: 33,595 / 35,716 / 37,140 / 36,833 / 34,734 / 26,400 | Methods T1 | YES | YES |
| 34 | Y1 M3 sample = 108,526 person-waves | Methods | 108,526 (Methods); 108,509 (Abstract) | NEAR-MATCH — Abstract says "108,509", Methods says "108,526". Discrepancy of 17 person-waves. |
| 35 | "1.31-hour residual" in Discussion limitations | Discussion | matches Results | YES |

────────────────────────────────────────────────────────────────────────────

ADDITIONAL DISCREPANCY NOT IN MAIN TABLE

[CRIT-TXT-003] Y1 M3 sample size mismatch
- Abstract: "the focal Y2 model and reduces the log-odds of access by 0.85" — and elsewhere in opening "Y1 spec ladder uses 148,599 person-waves in M1 and 108,526 person-waves in M2/M3"
- Methods §sample-disclosure: "108,526 person-waves in M2/M3"
- Methods earlier paragraph: "the focal M3 specification, which conditions on the full set of M3 covariates, retains 108,509 person-waves"
- Problem: Two different Y1 M3 sample sizes given in Methods (108,526 vs 108,509). One must be the typo. 17-person-wave discrepancy.
- Fix: Reconcile against the locked snapshot model-fit object's `nobs`.
- Severity: CRITICAL (small magnitude but contradiction inside Methods).

────────────────────────────────────────────────────────────────────────────

VERDICT

NEEDS-REVISION

Primary issues:
1. CRIT-TXT-001 — H3 cited p-value (0.92) attributed to triple-interaction row but per `limitations-accepted.md` Late-caught CRITs is the main-effect row; replace with corrected p from `adjudication-log.csv` `H3-CORRECTED` and re-derive verdict (in 4 sections).
2. CRIT-TXT-003 — Y1 M3 sample size internal contradiction (108,526 vs 108,509) within Methods.
3. WARN-TXT-001 — Reconcile Oaxaca total (0.82) vs raw gap (1.8) with one explanatory sentence.
4. WARN-TXT-003 — Soften the "ordered as cohort-as-cause predicts" claim or explain the interior non-monotonicity (1956-65 → 1966-75 → 1976-85).
5. WARN-TXT-002, WARN-TXT-005 — minor strengthening.
6. Causal-language audit — replace "reduces" with "is associated with a reduction of" in Abstract and Conclusion.

Secondary observation: numerical consistency across Abstract, Results, Discussion, and Conclusion is otherwise excellent (35 of 35 cross-section number checks match), with the H3 row-extraction issue being the dominant load-bearing error.

## 附录 J —— `verify-completeness` 报告（完整）

*文件：`output/digital-divide-china-cfps/` `verify/verify-completeness-2026-05-04.md`。Stage-2 完整性审计：产物链、marker 位置、孤儿检查、表格重新编号建议。判决：NEEDS-REVISION（1 CRIT, 5 WARN）。*

SCANNED: 30 raw artifacts, 10 manuscript artifacts (4 tables + 6 figures), 23 in-text references

###  VERIFICATION REPORT: ARTIFACT COMPLETENESS & CROSS-REFERENCE INTEGRITY

Project: digital-divide-china-cfps
Manuscript: drafts/draft-manuscript-digital-divide-china-cfps-2026-05-04.md
Locked snapshot: results-locked/2026-05-04-1722/
Date: 2026-05-04

---

#### SUMMARY

- Raw output files in locked snapshot: 30 artifacts (21 table-side files, 7 figure-side files, 2 verify files)
- Distinct figure assets (PDF): 6 (fig1...fig6)
- Distinct table assets (Y1 ladder, Y2 ladder, descriptives, oaxaca, intersection): 5 primary + many supporting registries
- Manuscript figures referenced (Figures 1-6): 6
- Manuscript tables referenced (Tables 1-4): 4
- "[X about here]" markers: 10 (Figures 1,2,3,4,5,6 + Tables 1,2,3,4)
- Full chain verified (raw -> manuscript -> text): 9/10
- Broken chains: 1 (Table 1 has dual identity — see CRIT-REF-001)

---

#### FULL ARTIFACT CHAIN MAP

| # | Locked Raw Output                                         | Manuscript Artifact          | Marker Line | First Discussion | Chain Status |
|---|-----------------------------------------------------------|------------------------------|-------------|------------------|--------------|
| 1 | figures/fig1-access-trend.pdf (+fig1-access-trend-data.csv)| Figure 1 (access trend)      | 111         | 113              | COMPLETE     |
| 2 | figures/fig2-Y2-by-cohort.pdf                              | Figure 2 (cohort trajectories)| 131        | 133              | COMPLETE     |
| 3 | figures/fig3-hukou-coef-trajectory.pdf                     | Figure 3 (Y1 wave coef)      | 121         | 123, 151         | COMPLETE     |
| 4 | figures/fig4-Y2-by-hukou-cohort.pdf                        | Figure 4 (Y2 by hukou*cohort)| 145         | 147, 153         | COMPLETE     |
| 5 | figures/fig5-oaxaca-decomp.pdf                             | Figure 5 (Oaxaca)            | 127         | 129              | COMPLETE     |
| 6 | figures/fig6-intersection-cells.pdf                        | Figure 6 (intersection cells)| 137         | 139              | COMPLETE     |
| 7 | tables/table1-descriptives.{csv,html}                      | Table 1 (descriptives) — see CRIT-REF-001 | 119 | 143       | DEGRADED     |
| 8 | tables/table-Y1-models.{csv,html,tex} (+y1-focal-hukou.csv,spec-registry-Y1.csv) | Table (Y1 ladder, no clean number) | (none) | 123 (mislabeled "Table 1") | BROKEN (no marker; mis-labeled) |
| 9 | tables/table-Y2-models.{csv,html,tex} (+y2-focal-hukou.csv,y2-ame.csv,spec-registry-Y2.csv) | Table 2 (Y2 ladder) | 115 | 117 | COMPLETE |
|10 | tables/oaxaca-decomp.csv                                   | Table 3 (Oaxaca)             | 125         | 129              | COMPLETE     |
|11 | tables/intersection-cells.csv                              | Table 4 (intersection cells) | 135         | 139              | COMPLETE     |
|12 | tables/{spec-registry,results-registry,fdr-focal,curation-plan,adjudication-log,missing-by-wave}.csv | (none — supporting registries) | — | — | INFO (orphaned in locked snapshot, but expected; SI/audit assets) |
|13 | verify/runtime-sanity-2026-05-04.md, verify/mt-correction-report.md | (none — audit notes) | — | — | INFO |

---

#### CRITICAL ISSUES

####### [CRIT-REF-001] Table 1 has dual identity / Y1 ladder lacks its own table number

The manuscript uses the label "Table 1" for two distinct artifacts:

1. Line 119 marker `[Table 1 about here]` followed (line 123) by prose:
   > "The corresponding access (Y1) ladder (Table 1) shows the predicted convergence pattern. The M1 rural-hukou logit coefficient is minus 1.71..."

   This refers to the Y1 model ladder (locked at `tables/table-Y1-models.{csv,html,tex}`).

2. Line 143 prose:
   > "Table 1 reports the descriptive composition of the analytic sample by hukou status. The rural-hukou subsample is on average 4.6 years older..."

   This refers to the descriptives table (locked at `tables/table1-descriptives.{csv,html}`).

Both content blocks exist as locked raw outputs, but the manuscript collapses them under one number. This is a **DUPLICATE NUMBER** problem AND an **UNREFERENCED ARTIFACT** problem simultaneously:
- Two physically distinct tables share the label "Table 1".
- The Y1 model ladder (`table-Y1-models.*`, the primary Y1 result asset) has no unambiguous number, no caption, and no `[Table N about here]` marker assigned to it specifically.
- The descriptives table has prose discussion (line 143) but no `[Table N about here]` marker (the line-119 marker is consumed by the Y1 ladder discussion at line 123).

Action: renumber. Recommended fix: relabel descriptives as Table 1, Y1 ladder as Table 2, Y2 ladder as Table 3, Oaxaca as Table 4, intersection-cells as Table 5; insert separate `[Table N about here]` markers for each; rewrite line 119–123 so the Y1 ladder gets its own marker and its own anchor sentence; or keep the descriptives implicit in the text and number Y1 ladder as Table 1 throughout. Either fix is acceptable but the current state ships two artifacts under one label.

Severity: CRITICAL.

---

#### WARNINGS

####### [WARN-REF-001] Figure 3 referenced before its marker
Line 121 inserts `[Figure 3 about here]` after Table 1 marker (line 119) but Figures 1 and 2 are intercalated with Table markers. The numbering is non-sequential by appearance:
- Marker order in prose: Fig 1 (111), Tab 2 (115), Tab 1 (119), Fig 3 (121), Tab 3 (125), Fig 5 (127), Fig 2 (131), Tab 4 (135), Fig 6 (137), Fig 4 (145).
- Reading order: Fig 1, Tab 2, Tab 1, Fig 3, Tab 3, Fig 5, Fig 2, Tab 4, Fig 6, Fig 4.

The "first mention rule" (artifacts referenced in numerical order) is violated. Tables: 2 before 1; Figures: 3 before 2, 5 before 4, 6 before 4. This will not block submission but copy-editors flag it.

Action: reorder markers/discussion or renumber figures and tables to match presentation order. Strongly recommended for Social Forces house style.

Severity: WARNING.

####### [WARN-REF-002] Figure 1 caption / Y2-trend reference uses "(Figure 1)" but data referenced not all in fig1
Line 113 attributes both the Y1 access trend AND the Y2 conditional-on-user means to "Figure 1". The locked `fig1-access-trend.pdf` plots Y1 access trend (the supporting CSV `fig1-access-trend-data.csv` confirms this is the access-trend asset). The Y2 mean rises (11.9 -> 14.7 hours) cited in prose are not visualized in fig1 — they appear to be derived from `tables/missing-by-wave.csv` or `y2-focal-hukou.csv` rather than from a figure.

Action: either add the Y2 trend to Figure 1 (paneled), reference Table 1/Table 2 for the Y2 numbers in line 113, or split into Figure 1a/1b.

Severity: WARNING.

####### [WARN-REF-003] Multiple supporting CSVs orphaned in locked snapshot
The locked snapshot contains supporting/registry CSVs not directly referenced by any manuscript figure or table number:
- `tables/spec-registry.csv` (referenced obliquely line 97: "the registry, together with the spec-by-spec adjudication log and the FDR-focal table, is archived in the locked results snapshot")
- `tables/spec-registry-Y1.csv`, `tables/spec-registry-Y2.csv`
- `tables/results-registry.csv`
- `tables/fdr-focal.csv`
- `tables/curation-plan.json`
- `tables/adjudication-log.csv`
- `tables/missing-by-wave.csv`
- `tables/y1-focal-hukou.csv`, `tables/y2-focal-hukou.csv`, `tables/y2-ame.csv`
- `figures/fig1-access-trend-data.csv` (data for Figure 1 — not orphaned, paired)

These appear to be SI / audit assets per line 97 ("archived in the locked results snapshot"). Recommend an explicit Supplementary Information appendix listing these so they are not silently orphaned.

Severity: WARNING.

####### [WARN-REF-004] No appendix / SI section in manuscript draft
The Methods section refers to robustness checks "reported in the robustness section" (line 89), to "supplementary material" (lines 97, 99, 105, 169), and to deferred items (Y3, log_pc_income, HAPC variance test). The draft has no Appendix or Supplementary Information section that would house these — the paper ends at line 189 References placeholder.

If "supplementary material" is a separate file to be authored later, this is acceptable but should be flagged in Phase 8 / submission packaging. If supplementary content was supposed to be inline, several locked artifacts (spec-registry, fdr-focal, missing-by-wave) belong there.

Severity: WARNING.

####### [WARN-REF-005] [CITATION NEEDED] markers used as numeric placeholders
The draft uses `[CITATION NEEDED]` after numerical estimates (e.g., line 117: "minus 1.31 [CITATION NEEDED] hours per week") rather than as bibliographic citations. This is an unconventional use of the marker — the underlying numbers are present and locked in `table-Y2-models.csv` and `y2-focal-hukou.csv`, so the marker semantics are misleading. Phase 8 references resolution will not change these numerics.

Action: either drop the `[CITATION NEEDED]` from numeric estimates (numbers are sourced from locked tables, no citation required) or replace with `[verified vs. table-Y2-models.csv]` so Phase 8 does not waste effort. The References section placeholder at line 189 is correctly marked.

Severity: WARNING (cosmetic, but will confuse the Phase 8 reference resolver).

---

#### CONTENT COMPLETENESS

| Manuscript Artifact | Marker present? | Caption/Title in draft? | Discussion within 30 lines? | Notes/N/Fit Stats? | Status |
|---------------------|-----------------|-------------------------|------------------------------|--------------------|--------|
| Figure 1            | YES (line 111)  | NO (no caption block)   | YES (line 113)               | N/A                | WARN: no caption |
| Figure 2            | YES (line 131)  | NO                      | YES (line 133)               | N/A                | WARN: no caption |
| Figure 3            | YES (line 121)  | NO                      | YES (line 123, 151)          | N/A                | WARN: no caption |
| Figure 4            | YES (line 145)  | NO                      | YES (line 147, 153)          | N/A                | WARN: no caption |
| Figure 5            | YES (line 127)  | NO                      | YES (line 129)               | N/A                | WARN: no caption |
| Figure 6            | YES (line 137)  | NO                      | YES (line 139)               | N/A                | WARN: no caption |
| Table 1 (descriptives) | NO (marker at 119 captured by Y1 ladder) | NO | YES (line 143, +24 lines from marker — within 30) | NO | CRIT-REF-001 |
| Table (Y1 ladder)   | shares marker 119 | NO                    | YES (line 123)               | NO                 | CRIT-REF-001 |
| Table 2 (Y2 ladder) | YES (line 115)  | NO                      | YES (line 117)               | NO                 | WARN: no caption/notes |
| Table 3 (Oaxaca)    | YES (line 125)  | NO                      | YES (line 129)               | NO                 | WARN: no caption/notes |
| Table 4 (intersection)| YES (line 135) | NO                     | YES (line 139)               | NO                 | WARN: no caption/notes |

Caption blocks (formal "Figure N. Title. Note: ..." structures) are missing for ALL figures and tables in the draft. This is a Phase 7b/8 task but should be flagged.

---

#### "[X about here]" MARKER -> PROSE WITHIN 30 LINES CHECK

| Marker (line) | Marker text | First prose mention | Distance | OK? |
|---------------|-------------|---------------------|----------|-----|
| 111 | [Figure 1 about here] | "(Figure 1)" line 113 | +2 | YES |
| 115 | [Table 2 about here]  | "(Table 2)" line 117  | +2 | YES |
| 119 | [Table 1 about here]  | "(Table 1)" line 123  | +4 | YES (but ambiguous artifact — see CRIT-REF-001) |
| 121 | [Figure 3 about here] | "Figure 3" line 123 ("wave-interacted Y1 variant (Figure 3)") | +2 | YES |
| 125 | [Table 3 about here]  | "(Table 3 on oaxaca-decomp..." line 129 | +4 | YES |
| 127 | [Figure 5 about here] | "Figure 5" line 129 | +2 | YES |
| 131 | [Figure 2 about here] | "Figure 2 plots..." line 133 | +2 | YES |
| 135 | [Table 4 about here]  | "(Table 4..." line 139 | +4 | YES |
| 137 | [Figure 6 about here] | "Figure 6" line 139 | +2 | YES |
| 145 | [Figure 4 about here] | "Figure 4 plots..." line 147 | +2 | YES |

All 10 markers have associated discussion within 30 lines. This check passes.

---

#### REFERENCES SECTION

Line 187-189:
```
#### References

[CITATION NEEDED] — to be resolved in Phase 8 from `citations/refs.bib`.
```

This matches the user's expected placeholder format. Phase 8 deferral is correctly flagged. PASS.

---

#### ORPHAN CHECK (locked artifacts not cited in prose)

Locked figures (PDF assets):
- fig1, fig2, fig3, fig4, fig5, fig6 — ALL CITED.
- No orphan figures.

Locked primary tables:
- table1-descriptives — cited (line 143)
- table-Y1-models — cited (line 123, mislabeled as "Table 1"; see CRIT-REF-001)
- table-Y2-models — cited (line 117 as "Table 2")
- oaxaca-decomp — cited (line 129 as "Table 3")
- intersection-cells — cited (line 139 as "Table 4")

Locked supporting/registry artifacts (not numbered tables; SI candidates):
- spec-registry.csv, spec-registry-Y1.csv, spec-registry-Y2.csv, results-registry.csv, fdr-focal.csv, curation-plan.json, adjudication-log.csv, missing-by-wave.csv, y1-focal-hukou.csv, y2-focal-hukou.csv, y2-ame.csv, fig1-access-trend-data.csv
- These are referenced collectively at lines 97 and 99 ("archived in the locked results snapshot," "we deferred Y3 from the headline and reserve it for a Phase 7b iteration") but not individually as Tables.

No primary-asset orphans. The supporting registries are SI-bound, not orphans.

---

#### SCRIPT TRACEABILITY

Manifest does not include a `scripts/` lock_dir; lock_dirs = ["tables","figures","eda","verify"]. Script-level traceability is not in scope for the locked snapshot at this lock_id and was not verified here. INFO only.

---

#### VERDICT

**NEEDS-REVISION**

Blocking issues (must fix before submission):
1. **CRIT-REF-001** — Table 1 dual identity. Resolution: renumber tables so the Y1 ladder and the descriptives table each have their own number, marker, and prose anchor. Recommended renumbering: Table 1 = descriptives, Table 2 = Y1 ladder, Table 3 = Y2 ladder, Table 4 = Oaxaca, Table 5 = intersection-cells (with corresponding Table-N-about-here marker reorder and in-text relabeling).

Non-blocking but recommended (can be deferred to Phase 7b/8):
2. WARN-REF-001 — Reorder markers/numbering to follow first-mention sequence.
3. WARN-REF-002 — Clarify what "Figure 1" depicts; the prose mixes Y1-trend (in fig1) and Y2-mean (not in fig1).
4. WARN-REF-003 — Add SI/Appendix listing the locked registry CSVs.
5. WARN-REF-004 — Decide whether SI is in-document or separate; if in-document, draft it.
6. WARN-REF-005 — Strip `[CITATION NEEDED]` markers attached to numeric estimates; they will confuse Phase 8.
7. Captions/notes for all figures and tables are missing in the draft body — add canonical "Figure N. Title. Note: data source, N, FE, SE structure" blocks.

The figure-side chain is fully clean (6/6 figures covered, all markers within 30 lines, no orphans). The table-side chain has one CRITICAL labeling collision that must be resolved before submission.

## 附录 K —— Windows 安装指引

这份附录存在的理由，是 §2 的安装命令默认你在类 Unix 的 shell 里。Windows 用户要先做三件事，§2 才能照搬：

1. 开启 **WSL2**（Windows Subsystem for Linux 2），并装好 **Ubuntu**；
2. 装 **Windows Terminal**，作为你日常使用的终端宿主；
3. 在 Ubuntu shell 里照 §2 与 §2.6 的命令一条条跑。

走完第 3 步，你就和 macOS / Linux 用户没区别了，本手册其余章节无需为 Windows 额外调整。

> **不要把 PowerShell、`cmd.exe` 或 Git-Bash 当成主用 shell。** Claude Code 与 Codex 在 Windows 原生上确实能跑，但 open-scholar-skill 的 PreToolUse hook 是一个 Bash 脚本，依赖 `jq` 和 `python3` 的 POSIX 语义。在 Windows 原生 shell 下 hook 会 fail-closed。WSL2/Ubuntu 给你一个真正的 Linux 内核 —— `bash`、`jq`、`python3`、`git`、`R`、技能插件的 symlink 都能原样工作。

### K.1 准备条件

- Windows 10（2004 版本 / 19041 build 及以上）或 Windows 11。
- 一个具有**管理员**权限的账户（一次性，用于装 WSL2）。
- 至少 10 GB 可用磁盘（Ubuntu 镜像约 2 GB，其余给 R + Python + 数据）。
- 安装阶段需要网络。

### K.2 第 1 步 —— 装 WSL2 与 Ubuntu

右键开始菜单 → **「Windows Terminal（管理员）」**（或 PowerShell 管理员），然后跑：

```powershell
PS> wsl --install -d Ubuntu-22.04
```

这一条命令会开启 WSL 功能、下载 WSL2 内核、装好 Ubuntu 22.04 LTS。**系统提示重启就重启。** 重启后 Ubuntu 安装器会自动弹出，要求你创建 Linux 用户名与密码（**与 Windows 登录是两码事**，挑一个简单的，以后 `sudo` 时要用）。

如果 `wsl --install` 提示已经装过 WSL，改成：

```powershell
PS> wsl --set-default-version 2
PS> wsl --install -d Ubuntu-22.04
PS> wsl --set-default Ubuntu-22.04
```

确认：

```powershell
PS> wsl -l -v
  NAME            STATE           VERSION
* Ubuntu-22.04    Running         2
```

`VERSION` 那一列必须是 `2`。如果是 `1`，跑一次 `wsl --set-version Ubuntu-22.04 2`，等几分钟转换完成。

### K.3 第 2 步 —— 装 Windows Terminal

Windows 11 自带 Windows Terminal。Windows 10 可以从 Microsoft Store 搜「Windows Terminal」安装，或在管理员 PowerShell 里：

```powershell
PS> winget install --id Microsoft.WindowsTerminal
```

打开 Windows Terminal，点新建标签 `+` 旁边的下拉箭头，能看到 **Ubuntu-22.04**。点它，进入一个真正的 Linux shell，提示符大概是：

```bash
yourname@DESKTOP-XYZ:~$
```

把 Ubuntu 设为默认，让新标签直接开 Linux：**设置 → 启动 → 默认配置文件 → Ubuntu-22.04**。

### K.4 第 3 步 —— Ubuntu 基础环境

在 Ubuntu shell 里一次性跑下面这些（和任何新装的 Ubuntu 一样）：

```bash
$ sudo apt update && sudo apt -y upgrade
$ sudo apt -y install build-essential curl wget unzip ca-certificates \
                       software-properties-common gnupg lsb-release \
                       jq python3 python3-pip python3-venv git
$ git --version && jq --version && python3 --version
```

这给了你 §2 所需的最低限度依赖。剩下 —— Node.js、Claude Code、Codex、open-scholar-skill 插件、R、社会科学包栈 —— 完全照搬 §2 与 §2.6 的命令，不用改。

### K.5 文件该放在哪儿

这是 Windows 用户最容易踩坑的地方。你现在有**两套**文件系统：

- **Windows 侧：** `C:\Users\yourname\...`（资源管理器里看得见）；
- **WSL2 / Ubuntu 侧：** `/home/yourname/...`（Linux 家目录，资源管理器默认看不到）。

规则：

- **项目目录放在 Linux 侧**（`/home/yourname/projects/digital-divide-china-cfps`）。在那里 I/O 比 `/mnt/c/Users/...` 快 5–20 倍，PreToolUse hook 也只在 Linux 文件系统上工作可靠。
- 想从资源管理器看 Linux 文件，把地址栏填成 `\\wsl$\Ubuntu-22.04\home\yourname`（Windows 11 上也可以是 `\\wsl.localhost\Ubuntu-22.04\...`）。拖拽与复制粘贴都正常。
- 想从 Ubuntu 里访问 Windows 文件（比如 `C:\Downloads` 里下好的数据集），路径是 `/mnt/c/Users/yourname/Downloads/`。**只用来做一次性的复制**（`cp /mnt/c/.../data.zip ~/projects/...`），不要直接在 `/mnt/c` 上跑分析。

### K.6 编辑器集成（VS Code）

绝大多数 Windows 学员会把 VS Code 当作编辑器，但文件其实在 WSL2 里：

1. 从 <https://code.visualstudio.com> 装 **VS Code for Windows**；
2. 装 **"WSL"** 扩展（发布者 Microsoft，ID 是 `ms-vscode-remote.remote-wsl`）；
3. 在 Ubuntu shell 里进项目目录，跑 `code .`。VS Code 会以 WSL 附加模式打开，左下角写着 "WSL: Ubuntu-22.04"。这扇窗口里的每个终端面板都已经在 Ubuntu 里。

**不要**从 Windows 原生 VS Code 通过 `\\wsl$\...` 直接开同一个项目；换行符与文件监听会混乱。

### K.7 然后回到 §2.6

走到这一步，你和一个 macOS/Linux 学员完全等价。**回到 §2.6 —— 「让智能体替你安装研究工具链」**，把四条提示词跑一遍。智能体会自动识别出 Ubuntu，使用 `apt` 路径。

§2.6.2 第 (1) 条提示词最后让你把 SSH 公钥贴到 GitHub —— 在 Windows Terminal 里直接：

```bash
$ cat ~/.ssh/id_ed25519.pub | clip.exe
```

`clip.exe` 因 WSL2 互操作机制位于 PATH 上，公钥会直接落到 Windows 剪贴板，可以马上粘进 github.com。

### K.8 Windows 原生安装（不推荐，但可行）

如果 IT 政策禁止开 WSL2，Claude Code 与 Codex 也能跑在 Windows 原生上。代价是：

- 从 <https://nodejs.org> 装 Node.js LTS（`.msi` 安装器会自动把 `npm` 加到 PATH）；
- `npm install -g @anthropic-ai/claude-code` 与 `npm install -g @openai/codex` 都能装；
- 用 **Windows Terminal + PowerShell 7+**（**不要**用旧版 `cmd.exe`）；
- 从 <https://git-scm.com/download/win> 装 **Git for Windows**。安装时选 "Use Git from the Windows Command Prompt"、"Checkout as-is, commit Unix-style line endings"；
- Python 从 <https://www.python.org/downloads/windows/> 装（勾选 "Add Python to PATH"）。R 从 <https://cran.r-project.org/bin/windows/base/> 加 RTools 装；
- `jq` 用 `winget install jqlang.jq` 装（PreToolUse hook 要用）；
- **PreToolUse hook 在 Windows 原生下不可用。** open-scholar-skill 的 hook 脚本是 Bash 写的，要么装 Git-Bash 并把 Claude Code 的 hook 配置改成走 `bash.exe`，要么承认 hook 不工作 —— **不要用这种配置处理涉敏感数据的项目**。

原生路线省了磁盘，但代价是数据安全闸门和统一的 shell。如果你要做涉真实参与者数据的研究，**用 WSL2**。

### K.9 Windows 常见坑

| 现象 | 原因 | 解决 |
| ---- | ---- | ---- |
| `npm install -g ...` 后 WSL2 里找不到 `claude` | 全局 npm 安装到了 `~/.npm-global/bin`，但没加 PATH | `echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc && exec bash` |
| 跑 setup.sh 报 `bash: jq: command not found` | Ubuntu 里没装 `jq` | `sudo apt install jq` |
| 在 `/mnt/c/...` 工作时 I/O 很慢 | 跨文件系统访问 | 把项目挪到 `/home/yourname/projects/` |
| PreToolUse hook 总是拦截文件 | 项目在 `/mnt/c/...`；路径规范化和 `.claude/safety-status.json` 对不上 | 把项目挪到 `/home/yourname/...`，重跑 `/scholar-init` |
| RStudio 在 WSL2 里启动不了 | RStudio 是 GUI，WSL2 GUI 支持在 Win11 上还行，Win10 上较脆弱 | 直接装 **Windows 原生 RStudio**；除非你很清楚自己在做什么，不要让它去连 WSL2 里的 R |
| `git diff` 满屏行尾差异 | Windows CRLF vs. Unix LF | `git config --global core.autocrlf input` |

### K.10 验证 Windows 安装

一个成功的 Windows 安装，最后应该能在 Windows Terminal → Ubuntu-22.04 标签 → 项目目录里跑出这套握手：

```bash
$ wsl -l -v          # （这条在 PowerShell 里跑）VERSION 必须是 2
$ uname -a            # Linux DESKTOP-...  5.x.x ... GNU/Linux
$ node --version      # v20.x.x
$ claude --version    # 2.0.x
$ codex --version     # 0.x.x
$ jq --version        # jq-1.6 或以上
$ pwd                 # /home/yourname/projects/...
```

如果六条都输出正常，回到 §2.4 装 open-scholar-skill 插件。从那以后，Windows 用户与本手册其他章节同步前进。
{% endraw %}
