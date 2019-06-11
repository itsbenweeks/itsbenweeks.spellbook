CloudZero Technical Challenge
---

### Technical interview introduction:

We find that interviews can be stressful, and generally at your job you aren’t solving problems under that kind of stress.  To allow people showcase their skills in a more natural environment, we’ve created a take-home problem that we ask candidates to solve. These problems should allow people to demonstrate how they solve problems with code, which is what anyone joining the engineering team would do day to day.

While we recognize that a take home problem has its own downsides, chief among them it’s a non-trivial request on time from people who are already busy (see below for other options,) we believe that any interview process requires a significant time commitment and this is one that gives us a better objective measure of how candidates would solve the types of problems necessary to thrive at CloudZero.

Please note, if you feel that you cannot find the time to work on the below problem then we will happily facilitate one of two other options.

First, if you have code that you can send us (an open source project, or something you’ve worked on for an employer or client that you can share,) feel free to send us that.  We ask that it show off your ability with Python and AWS and be something that you were the primary decision maker and coder on.  Please also ensure that it is something we can execute ourselves.

The second option is that we will allow you to pair-program a problem during one hour of the interview process.  The problem will be given to you at the interview, and we’ll help with a laptop and IDE and an engineer to pair with. 

Please indicate your preference between these three options as early as possible so that we can plan for a good experience.

### The problem:
For the problem below, we’d like you produce code that solves the problem and get it to us before we have you come in so that we can evaluate the solution. We will review the output with you when you come in. Sending us to a GitHub repo is probably easiest, but if you prefer getting us your solution in another way that is fine as well. Take the time you need and feel free to reach out if any part of the problem is unclear.

Using Python 3.6+, create a system that analyzes the Alexa top 1,000 sites.  The analysis should include:
 * Per Site
 * Word count of the first page and rank across all the sites based off the word count
 * Duration of the scan
 * Across All Sites
 * AVG word count of the first page
 * Top 20 HTTP headers and the percentage of sites they were seen in
 * Duration of the entire scan

You may use any library or AWS service that you desire as long as your system is installable by us.  Don't over-engineer the solution; keep it simple, elegant and functional.  Your solution should run to completion within 15 minutes.

Please be aware, the cost for calling some AWS services and APIs can add up quickly.  You may want to watch that as you develop so that you don't incur an unexpectedly expense during development!