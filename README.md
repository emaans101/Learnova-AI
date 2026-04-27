# Learnova AI

Learnova AI is a prototype AI-powered platform designed for schools to support both student learning and teacher awareness in a safe, privacy-focused way. The platform gives teachers a high-level, real-time view of student AI interactions without exposing private conversations unless intervention is necessary.

The goal of the project is to create a balanced classroom experience where AI helps students learn more effectively, while also giving educators the tools to notice academic struggles, safety concerns, and engagement patterns early.

## Project Overview

Learnova AI is built around two connected experiences:

- `Student Mode` supports learning, study planning, assignments, and progress tracking.
- `Teacher Mode` provides visibility into classroom trends, student wellbeing indicators, and learning progress.

This project is currently a prototype intended to demonstrate the product concept, user experience, and core workflow ideas.

## Core Features

### 1. Safe classroom AI monitoring

Teachers can view real-time indicators related to student AI use in a privacy-conscious format. Instead of exposing full conversations by default, the system highlights patterns and signals such as:

- Safety scores
- Bias flags
- Distress alerts
- Off-curriculum responses
- Students who may be struggling

This allows educators to stay informed without unnecessarily reading private student interactions.

### 2. Distress detection and escalation

If a student expresses distress, for example by saying something like "I want to give up," the platform is designed to:

1. Automatically detect and flag the message
2. Send a supportive response to the student
3. Privately alert the teacher or school counselor for follow-up

This feature is intended to help schools respond quickly and responsibly when students may need support.

### 3. Personalized study timeline generation

Students and teachers can upload study materials, notes, or syllabi. Based on that content, the AI can generate personalized study timelines to help students:

- Stay organized
- Prepare ahead of deadlines
- Focus on important material
- Work toward higher grades

### 4. Subject-based progress tracking

The platform includes progress tracking with visual indicators so both students and teachers can monitor performance across subjects. This helps identify:

- Strong subjects
- Weak areas
- Learning trends over time
- Suggestions for improvement

### 5. AI-guided assignment support

Learnova AI is designed to support learning rather than simply give answers. For assignments such as essays or written work, the AI guides students step by step by:

- Asking helpful questions
- Breaking tasks into manageable parts
- Encouraging independent thinking
- Supporting better understanding of the process

### 6. Anonymous motivation systems

To encourage consistent effort, the platform includes an anonymous leaderboard based on task completion. This is intended to keep students motivated while avoiding unnecessary public comparison.

## Prototype Scope

This repository represents a prototype version of Learnova AI. The current focus is on:

- Interface design
- Dashboard concepts
- Student and teacher workflow ideas
- AI-assisted learning and safety concepts

It is not yet a full production-ready system.

## Repository Structure

```text
Learnova-AI/
├─ assets/              # Images and static assets
├─ css/                 # Frontend styles
├─ docs/                # Project documentation
├─ pages/               # Prototype page structure
├─ chatbot.html         # Chatbot UI prototype
├─ chatbot.py           # Flask chatbot backend prototype
├─ config.py            # App configuration
├─ database.py          # Database-related logic
├─ index.html           # Main dashboard prototype
├─ resources.html       # Resources page prototype
├─ main.py              # Placeholder Python entry file
└─ requirements.txt     # Python dependencies
```

## Tech Direction

The current prototype includes:

- Static frontend pages in HTML and CSS
- A Python backend prototype using Flask
- Early project structure for future student and teacher experiences

## Future Improvements

Planned areas for future development may include:

- Full Teacher Mode and Student Mode workflows
- Secure authentication and role-based access
- Live dashboards backed by real data
- Safer alert escalation workflows
- File upload and study-plan generation pipelines
- Improved analytics and progress reporting
- Better integration between frontend and backend services

## Vision

Learnova AI is designed to show how AI can be used in education not just to answer questions, but to support safety, structure, motivation, and growth. The long-term vision is a school-friendly platform that helps students succeed while giving educators the insight they need to intervene thoughtfully and responsibly.
