# Syllabus

Please read this syllabus carefully at the beginning of the class, and return to it as often as necessary.

## Learning outcomes

This class aims at teaching **modern programming techniques** for (geo-)scientists. After completing the class and actively participating throughout the semester, you will:
- be familiar with a modern and open-source programming language (Python) and its use for scientific applications
- be able to program in a structured, extendable, and reproducible manner
- be able to read and write Python programs of intermediate complexity, as well as Python packages
- understand how numbers are handled by computers and be aware of numerical accuracy errors 
- be aware of simple performance considerations
- know how to write and run formal tests for your code
- be acquainted with various programming utility tools: IDEs, debugger, AI
- be able to search for, understand, install and take advantage of existing packages and libraries available in the rich scientific Python ecosystem


```{admonition} Non-objectives of this class:

This class is not about learning data analysis, plotting or numerics. Nor is it about learning the details of the Python packages you will use for the rest of your studies such as matplotlib, pandas, xarray, etc, although we will be using some of these packages. 

The objective here is to provide you with a **solid foundational knowledge about core programming concepts**, in order to make you an **independent learner**, able to expand and deepen your programming skills by yourself.

Don't worry: you will have ample time to play with fancy libraries in this and other classes of the program.
```

## Prerequisites

The targeted audience for this course are **students at the MSc level with previous experience in programming**. No prior knowledge of Python is required, but it is assumed that you are familiar with a similar language (MATLAB, IDL, R...) and basic programming structures (e.g., loops, functions, conditional blocks). 

Ideally, you will have the programming level of a student having completed <a href="https://lfuonline.uibk.ac.at/public/lfuonline_lv.details?sem_id_in=25S&lvnr_id_in=707638&sprache_in=en">the introduction to programming for atmospheric scientists</a> in your BSc program. The first few units will be catching up on the materials from the BSc class, but quickly enough we will move towards more advanced topics.

## Organisation of the class

The class is taught in English. It is, however, okay to ask questions in German.

The class follows the [flipped classroom](https://en.wikipedia.org/wiki/Flipped_classroom) concept. This means that you will acquire new knowledge at home by reading online materials (and watching videos when appropriate). We will then use the time together in class to discuss the materials and write code.

**Each week of the semester is organized as follows**:
- On Monday after class, you will receive the lecture notes for the following week (materials to read, a quiz, and the programming assignments). You study the materials until Monday and answer the quiz questions. The quizzes are intended for you to see if you have understood the new material correctly. 
- On Monday (08:15-09:00), we meet and (mostly) discuss the assignment solutions from the previous week (one assignment presentation is mandatory but not graded, see "Grading" below) and to discuss the quiz. The discussion will be based on the short online quizzes and on the questions you bring to the classroom. 
- On Thursday (08:15-10:00), we meet to work on exercises and the assignments. 

There may be some deviations from the above schedule because of public holidays and to better accommodate some of the course content.

```{important}
You will receive 5 ECTS if you pass the course: with 1 ECTS corresponding to 25 hours of work, this represents 8-9 hours of work per week (15 weeks). For this course, it means that you are expected to spend more time working independently at home than in class.

It is strongly recommended that you work regularly for the class. Programming is quite different from other disciplines, and "doing nothing for a few months" cannot be replaced by a "no-sleep-48-hours-push" at the end of the semester. Programming is a bit like learning how to ski or climb: it is best learned by doing, and you will notice that regular practice will make you better each week.
```

## Learning checklist

At the end of each lesson, there is a "learning checklist": go over it at the end of the lecture and see if you can check all the boxes. It is a good way for you to check if you are ready to go on, or if you still need to go back to some reading and learning!

## Use of AI

AI has become an integral component of programming. It can also be a great tool to enhance learning. As such we will cover the use of AI in the course to some degree. You are also allowed to use AI tools unless explicitly prohibited (e.g., during exams). In light of academic integrity, you are also required to take full responsibility for all your submitted work (e.g., the semester project). AI does not always provide correct solutions either and you need to be a good-enough programmer to detect and correct potential problems (even with the help of AI). You thus need a solid foundation in programming to best work with AI tools. This course is intended to provide you with these skills. You will, however, only acquire them if you actively engage with the material and assignments and not if you let AI just write the code for you.

## Grading 

Your final grade will be a combination of a mid-term exam (20%), a final exam (50%), and a programming project (30%). Participation in both exams, handing in and presenting the programming project, at least one assignment presentation, and completing at least 50% of the quizzes are necessary to pass the class. At the beginning of the course, you will be assigned to small groups of 3-5 students. For the programming project and the assingment presentations, you will work in these groups.

1. The **mid-term exam** (open-book exam, combination of muliple choice, essay, and programming questions) will take place on **Thursday 26.11.2025** from 08:15 to 10:00.
2. The **final exam** (open-book exam, combination of muliple choice, essay, and programming questions) will take place on **Thursday 04.02.2026** from 08:15 to 10:00.
3. Each week you will be given a short **quiz** to test your understanding of the lecture material. You will have to fill out the quiz prior to the in-class discussion (usually Monday classes). The quizzes are not graded, but you need to complete at least half of the quizzes for a positive grade (submitted the latest 15 min before the class start time).
4. Each week there will be an **assignment** (unless specified otherwise, e.g. while you are working on the group project). These assignments can be worked through alone or in groups. The assignments will be discussed on Mondays and, each week, one or two groups will be asked to present their results to the rest of the class. The presentation is not graded, but participation and at least one group presentation are required to pass the class. Further information about the style of the presentations will be provided in class.
5. After the midterm, you will be assigned a **programming project**, on which you will work as a group over a few weeks. You will have to present your code packages to the class on **28.01.2025** and hand in the final packages before the presentation. To make sure that you make good progress on your project and to receive feedback while you are working on your code, there will be intermediate deadlines that will be announced later. Your project grade will consist of an individual component (50%) and a group component (50%).

## Weekly lesson plan 

This is a tentative schedule, which may change slightly during the semester.

- Week 01 (Mon 05/Thu 08 Oct) - Welcome and getting started with Python (installation, IDEs)
- Week 02 (Mon 12/Thu 15 Oct) - Python fundamentals
- Week 03 (Mon 19/Thu 22 Oct) - *Assignment 02*, Variable scopes, modules, and file paths
- Week 04 (Thu 29 Oct) - *Assignment 03*, Floating point arithmetics
- Week 05 (Thu 05 Nov) - *Assignment 04*, Numpy arrays and the scientific python stack (pandas, matplotlib)
- Week 06 (Mon 09/Thu 12 Nov) - *Assignment 05*, Programming style and AI
- Week 07 (Mon 16/Thu 19 Nov) - *Assignment 06*, *Revision*
- Week 08 (Mon 23/Thu 26 Nov) - Code documentation, **Mid-term exam (26 Nov)**
- Week 09 (Mon 30 Nov/Thu 03 Dec) - Code testing
- Week 10 (Mon 07/Thu 10 Dec) - *Assignment 08*, Python packages
- Week 11 (Mon 14/Thu 17 Dec) - *Assignment 09*, Group Project
- Week 12 (Mon 11/Thu 14 Jan) - Object Oriented Programming
- Week 13 (Mon 18/Thu 21 Jan) - *Assignment 10*, Object Oriented Programming
- Week 14 (Mon 25/Thu 28 Jan) - *Assignment 11*, **Final project submission** and **Project presentations**
- Week 15 (Mon 01/Thu 04 Feb) - **Final exam (4 Feb)**
