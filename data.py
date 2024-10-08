import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate sample data
n_employees = 500
n_resources = 100
n_interactions = 4000

# Generate employee data
employees = pd.DataFrame({
    'employee_id': np.arange(1, n_employees + 1),
    'job_role': np.random.choice([
        'Software Development Engineer',
        'Product Manager',
        'Data Scientist',
        'Operations Manager',
        'HR Specialist',
        'Financial Analyst',
        'Marketing Specialist'
    ], n_employees),
    'past_activities': np.random.randint(0, 21, n_employees),
    'feedback_score': np.random.randint(1, 6, n_employees)
})

# Generate item data
resources = pd.DataFrame({
    'resource_id': np.arange(1, n_resources + 1),
    'resource_type': np.random.choice(['Video', 'Article', 'Course'], n_resources),
    'difficulty_level': np.random.choice(['Beginner', 'Intermediate', 'Advanced'], n_resources),
    'popularity_score': np.random.randint(1, 101, n_resources)
})

# Generate interactions data
interactions = pd.DataFrame({
    'employee_id': np.random.choice(employees['employee_id'], n_interactions, replace=True),
    'resource_id': np.random.choice(resources['resource_id'], n_interactions, replace=True),
    'interaction_score': np.random.randint(1, 5, n_interactions)
})

print(employees.head())
print(resources.head())
print(interactions.head())
