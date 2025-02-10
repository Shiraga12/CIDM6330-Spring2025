# Smart Task Management System  

## Front Matter  

**Course:** CIDM 6330 - Spring 2025  
**Assignment:** Assignment 01 - From Selection to Specification  
**Author:** Toluwani Adeoti  
**Date:** 2/12/25  

---

## Front Page  

# Smart Task Management System  
*A Productivity Enhancement Tool*  

**Developed by:** Toluwani Adeoti  
**Course:** CIDM 6330 - Spring 2025  
**Instructor:** Dr. Jeffry Babb  
**Date:** 2/12/25  

---

## Table of Contents  

1. [Introduction](#introduction)  
2. [Requirements Statements](#requirements-statements)  
3. [User Stories, Use Cases, Features, Gherkin Validation](#user-stories-use-cases-features-gherkin-validation)  
4. [Specifications](#specifications)  
   - [Concept](#concept)  
   - [UX Notes](#ux-notes)  
   - [Interfaces (Controls)](#interfaces-controls)  
   - [Behaviors](#behaviors)  
   - [Feature/Package A](#featurepackage-a)  
   - [Feature/Package N](#featurepackage-n)  
5. [UML Diagrams](#uml-diagrams)  

---

## Introduction  

### Problem Statement  
Task management is a challenge for individuals and teams juggling multiple responsibilities. Traditional methods such as paper-based planners or scattered digital notes often result in missed deadlines, disorganized schedules, and reduced productivity.  

### Domain of Practice  
This problem is prevalent in **personal productivity, business operations, and academic planning**. An effective task management solution can significantly improve workflow efficiency, prioritization, and accountability.  

### Personal/Professional Interest  
As a software developer, I am passionate about building solutions that enhance efficiency and organization. This project aims to explore user needs and design considerations for an intelligent task management system.  

### Proposed Software System  
The **Smart Task Management System** is designed to provide:  
- Task creation, categorization, and prioritization  
- Reminders and deadline tracking  
- Progress monitoring and reporting  
- Calendar integration and notifications  

---

## Requirements Statements  

### Functional Requirements  
1. The system shall allow users to create, edit, and delete tasks.  
2. The system shall enable users to set due dates and reminders.  
3. The system shall provide task categorization options (e.g., Work, Personal, School).  
4. The system shall allow task prioritization (High, Medium, Low).  
5. The system shall track task completion status.  

### Non-Functional Requirements  
1. The system shall provide a user-friendly interface accessible via web and mobile.  
2. The system shall store user data securely.  
3. The system shall support multi-user collaboration for shared task management.  
4. The system shall integrate with third-party calendar applications.  
5. The system shall load task data within 2 seconds for an optimal user experience.  

---

## User Stories, Use Cases, Features, Gherkin Validation  

### User Stories  
- **As a user,** I want to create tasks with due dates so that I can keep track of my schedule.  
- **As a user,** I want to categorize my tasks to organize them efficiently.  
- **As a user,** I want to receive notifications for upcoming deadlines so that I don’t forget important tasks.  

### Use Cases  

#### Use Case 1: Create a New Task  
**Actors:** User  
**Description:** The user creates a new task with a title, due date, and priority.  
**Preconditions:** The user must be logged into the system.  
**Flow:**  
1. The user clicks the "Create Task" button.  
2. The system displays a task creation form.  
3. The user enters task details and clicks "Save".  
4. The system stores the task and updates the task list.  
**Postconditions:** The new task appears in the user’s task list.  

### Gherkin Validation  

```gherkin
Feature: Task Creation
  Scenario: User creates a new task
    Given the user is logged in
    When the user clicks "Create Task"
    And enters task details
    And clicks "Save"
    Then the system saves the task
    And displays it in the task list
