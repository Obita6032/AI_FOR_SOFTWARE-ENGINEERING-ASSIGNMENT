# AI_FOR_SOFTWARE-ENGINEERING-ASSIGNMENT

1. Short Answer Questions
Q1: Explain how AI-driven code generation tools (e.g., GitHub Copilot) reduce development time. What are their limitations?
Answer:
>> AI-driven code generation tools like GitHub Copilot reduce development time by:
>> Autocompleting code snippets based on context.
>> Generating entire functions or classes from comments.
>> Reducing boilerplate and repetitive coding.
>> Helping junior developers learn faster by example.

Limitations:
>> May produce syntactically correct but logically incorrect code.
>> Lacks deep understanding of business rules or project architecture.
>> Can introduce security flaws if not reviewed.
>> Risk of code plagiarism from training data if used carelessly.
>>
Q2: Compare supervised and unsupervised learning in the context of automated bug detection.

| Aspect          | Supervised Learning                                         | Unsupervised Learning                                       |
| --------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| **Definition**  | Learns from labeled data (e.g., bug vs. no bug)             | Finds patterns in unlabeled data                            |
| **Example Use** | Classifying whether code contains bugs                      | Clustering unusual error logs                               |
| **Application** | Training a model on bug-labeled commits to predict new bugs | Identifying anomalies in system logs that deviate from norm |
| **Limitation**  | Requires large labeled datasets                             | May generate false positives or ambiguous clusters          |


Q3: Why is bias mitigation critical when using AI for user experience personalization?

Answer:
>> Bias mitigation is essential because:
>> AI models trained on skewed data may discriminate against users based on age, gender, region, etc.
>> Personalization algorithms may reinforce stereotypes or marginalize minority groups.
>> Biased experiences degrade user trust and platform fairness.
>> Ensures that all users receive equitable access to content, recommendations, and support.

2. Case Study Analysis
Article Summary: AI in DevOps: Automating Deployment Pipelines

Q: How does AIOps improve software deployment efficiency? Provide two examples.
Answer:
AIOps (Artificial Intelligence for IT Operations) improves software deployment by:
Predicting and resolving issues before they impact production.
Automating routine tasks like testing, monitoring, and rollback.
Providing real-time anomaly detection and root cause analysis.
Example 1:
AIOps tools monitor log streams to detect unusual behavior during deployment and automatically trigger rollback scripts.
Example 2:
Using ML to optimize resource allocation and scheduling for cloud deployments, reducing latency and cost during scaling.

