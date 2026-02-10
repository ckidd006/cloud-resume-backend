Christian Kidd's Cloud Resume Website

My personal project: A secure website hosting my resume, built on AWS. It shows cloud tech, coding, and security.

> (https://www.ckiddresume.com/) <

  
  What This Project Does: 
  
- Shows my resume in a nice web page with HTML, CSS, and Javascript.
- Counts visitors automatically (no manual work—uses back-end).
- Updates itself when I change code (automation via GitHub).


Tools I Used & Why:

- Front-End: HTML/CSS/JS on Visual Studio. Why? Makes the site look good and work on phones. JS calls a secure API for the counter (no hacking risk).
- Hosting: AWS S3 (stores files cheaply), CloudFront (makes it fast & secure with HTTPS). DNS Management.
- Back-End: DynamoDB (database for counter), API Gateway (safe door to back-end), Lambda (runs Python code serverless—no servers to hack).
- Automation: GitHub Actions (auto-deploys on code push). Tests Python code first to catch bugs.
- Security Focus: HTTPS everywhere, no direct database access, least permissions.


What I Learned:
  
- Serverless is cheap and secure, but setup needs care (IAM roles).
- CI/CD saves time—push code, it deploys auto.
- Important to secure
