---

# ⚙️ EnginCrew – Autonomous Multi-Agent Engineering

“Where AI Engineers Build Together”

Welcome to **EnginCrew**, a cutting-edge project powered by crewAI.
EnginCrew brings together a team of **autonomous AI agents** — engineering lead, backend engineer, frontend engineer, and test engineer — to design, build, and test software in a **collaborative, human-like workflow**.

Think of it as your **AI-powered engineering team**, working seamlessly to transform ideas into production-ready solutions.

---

## 🚀 Features

* 🧠 **Engineering Lead** – plans tasks and aligns objectives.
* ⚙️ **Backend Engineer** – builds scalable backend systems with safe code execution (Docker).
* 🎨 **Frontend Engineer** – creates user-facing interfaces with precision.
* 🧪 **Test Engineer** – validates code through autonomous testing.
* 🔄 **Sequential Workflow** – tasks are executed in a structured, team-like process.

---

## 🛠 Installation

Ensure you have **Python >=3.10 <3.14** installed.
This project uses [UV](https://docs.astral.sh/uv/) for smooth dependency management.

### 1️⃣ Install UV

```bash
pip install uv
```

### 2️⃣ Install Dependencies

Navigate to your project folder and install requirements:

```bash
crewai install
```

---

## ⚓ Safe Code Execution with Docker

Some agents (like Backend & Test Engineers) execute code safely using Docker.

### Install Docker Desktop (One-Click)

* [Download Docker Desktop](https://docs.docker.com/desktop/)
* Follow the installation instructions for your OS.

Once Docker is installed and running, EnginCrew agents can **safely execute and validate code** without risk to your local system.

---

## ⚙️ Customization

Configure EnginCrew to fit your project needs:

* **Agents** → `config/agents.yaml`
* **Tasks** → `config/tasks.yaml`
* **Crew Logic** → `src/engineering_team/crew.py`
* **Custom Inputs** → `src/engineering_team/main.py`

You’ll also need to add your **API keys** (e.g., `OPENAI_API_KEY` or `GROQ_API_KEY`) into your `.env` file.

---

## ▶️ Running EnginCrew

Kickstart your AI engineering team from the root folder:

```bash
crewai run
```

This command initializes the **EnginCrew**, assembling the agents and assigning tasks.
By default, it generates a `report.md` with insights/output in the project root.

---

## 🧩 Understanding Your Crew

The **EnginCrew** is composed of specialized AI agents:

* **Engineering Lead** → orchestrates project flow.
* **Backend Engineer** → handles logic, APIs, and databases.
* **Frontend Engineer** → manages design and user interaction.
* **Test Engineer** → ensures quality and stability.

Together, they mimic a real-world engineering team to **design, develop, and deliver** software autonomously.

---

## 📚 Support

For support, questions, or feedback regarding **EnginCrew** or [crewAI](https://crewai.com):

* 📖 Explore the [Documentation](https://docs.crewai.com)
* 🐙 For More via [GitHub](https://github.com/sakshi27maharana)

---

💡 **EnginCrew** is more than a framework — it’s your **autonomous engineering partner**, designed to supercharge productivity and creativity.

---
