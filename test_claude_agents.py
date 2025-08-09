#!/usr/bin/env python3
"""
Test script for Claude Code agents - allows manual testing and validation
of agent prompts and responses directly in the terminal.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()

# Add agents directory to path
agents_dir = Path(__file__).parent / "agents"
sys.path.append(str(agents_dir))

class AgentTester:
    """Base class for testing Claude agents with consistent API calls"""
    
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
        if not os.getenv('ANTHROPIC_API_KEY'):
            print("⚠️  Warning: ANTHROPIC_API_KEY not found in environment")
            print("   Create a .env file with your API key to test agents")
    
    def call_claude(self, prompt, model="claude-3-sonnet-20240229", max_tokens=1024):
        """Make a call to Claude with the given prompt"""
        try:
            response = self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error calling Claude: {e}"

    def run(self, prompt):
        raise NotImplementedError("Subclasses must implement the 'run' method.")

class ScrumMasterAgent(AgentTester):
    """AI Scrum Master Agent for automated sprint management"""
    
    def run(self, prompt):
        full_prompt = f"""
        You are an AI Scrum Master running a 3-hour automated standup.
        
        {prompt}
        
        Generate a comprehensive standup report including:
        - Sprint progress and velocity
        - Completed tasks since last standup
        - Currently active work
        - Any blockers detected
        - Action items for the team
        - Team health metrics
        
        Context: Frontend React team working on a user dashboard feature.
        Sprint has 3 days remaining with 8 story points completed out of 15 planned.
        """
        
        return self.call_claude(full_prompt)

class SprintPlanningAgent(AgentTester):
    """Sprint Planning Agent for backlog management and sprint setup"""
    
    def run(self, prompt):
        full_prompt = f"""
        You are a Sprint Planning Agent responsible for creating detailed sprint plans.
        
        {prompt}
        
        Generate a 2-week sprint plan for a development team including:
        - Sprint goals and success criteria
        - User stories with effort estimates
        - Task breakdown and dependencies
        - Risk assessment and mitigation
        - Definition of done criteria
        
        Context: Building a new authentication system for a SaaS platform.
        Team capacity: 3 developers, 1 designer, 1 QA engineer.
        """
        
        return self.call_claude(full_prompt)

class RetrospectiveAgent(AgentTester):
    """Retrospective Agent for sprint analysis and improvement recommendations"""
    
    def run(self, prompt):
        full_prompt = f"""
        You are a Retrospective Agent facilitating a sprint retrospective.
        
        {prompt}
        
        Generate a retrospective analysis including:
        - What went well during the sprint
        - Areas for improvement
        - Action items for next sprint
        - Team satisfaction metrics
        - Process optimization recommendations
        
        Context: Just completed a 2-week sprint with mixed results.
        Delivered 12/15 story points, had 2 major blockers, team worked overtime.
        """
        
        return self.call_claude(full_prompt)

class DailyStandupAgent(AgentTester):
    """Daily Standup Agent for collecting team updates and progress tracking"""
    
    def run(self, prompt):
        full_prompt = f"""
        You are a Daily Standup Agent collecting team member updates.
        
        {prompt}
        
        Generate individual standup updates for a 4-person development team:
        - Yesterday's accomplishments
        - Today's planned work
        - Any blockers or impediments
        - Help needed from team members
        
        Context: Mid-sprint development of an e-commerce checkout flow.
        Team includes: Frontend dev, Backend dev, DevOps engineer, QA tester.
        """
        
        return self.call_claude(full_prompt)

class CodeReviewerAgent(AgentTester):
    """Expert code reviewer focusing on quality, security, performance, and best practices"""
    
    def run(self, prompt):
        full_prompt = f"""
        You are an expert code reviewer with a keen eye for quality, security, and maintainability.

        {prompt}

        ## Review Focus Areas

        ### Code Quality
        - Readability and clarity
        - Naming conventions
        - Code organization and structure
        - DRY (Don't Repeat Yourself) principle
        - SOLID principles adherence
        - Design pattern usage
        - Technical debt identification

        ### Security Review
        - Input validation and sanitization
        - SQL injection vulnerabilities
        - XSS prevention
        - Authentication and authorization flaws
        - Sensitive data exposure
        - Dependency vulnerabilities
        - OWASP Top 10 compliance

        ### Performance Analysis
        - Algorithm complexity (Big O)
        - Database query optimization
        - Memory leaks and management
        - Caching opportunities
        - Async/concurrent programming issues
        - Network request optimization
        - Bundle size and load time

        ### Testing Coverage
        - Unit test coverage
        - Integration test adequacy
        - Edge case handling
        - Error scenario testing
        - Mock and stub usage
        - Test maintainability

        ### Documentation
        - Code comments clarity
        - API documentation
        - README completeness
        - Inline documentation
        - Change log updates

        ## Review Process
        1. Understand the context and requirements
        2. Check functionality against specifications
        3. Review code structure and organization
        4. Identify security vulnerabilities
        5. Analyze performance implications
        6. Verify test coverage
        7. Check documentation completeness
        8. Provide actionable feedback

        ## Feedback Style
        - Be constructive and specific
        - Provide code examples for improvements
        - Explain the "why" behind suggestions
        - Prioritize issues (critical, major, minor)
        - Acknowledge good practices
        - Suggest learning resources when relevant

        ## Common Issues to Check
        - Race conditions
        - Null pointer exceptions
        - Resource leaks
        - Hardcoded values
        - Inconsistent code style
        - Unnecessary complexity
        - Missing input validation

        ## Output Format
        ```markdown
        ## Code Review Summary
        - Overall Assessment: [Excellent/Good/Needs Improvement]
        - Critical Issues: [Count]
        - Suggestions: [Count]

        ### Critical Issues
        1. [Issue description and location]
           - Impact: [Description]
           - Suggestion: [Fix recommendation]

        ### Major Issues
        [List of major issues]

        ### Minor Suggestions
        [List of improvements]

        ### Positive Observations
        [Good practices noted]
        ```
        """
        
        return self.call_claude(full_prompt)

class TestAutomatorAgent(AgentTester):
    """Test Automator Agent for generating comprehensive test suites"""
    
    def run(self, prompt):
        full_prompt = f"""
        You are a Test Automator Agent creating comprehensive test suites.
        
        {prompt}
        
        Include:
        - Happy path test cases
        - Error handling scenarios
        - Edge cases and boundary conditions
        - Mock setup and teardown
        - Test data fixtures
        
        Use Jest/JavaScript testing framework.
        """
        
        return self.call_claude(full_prompt)

class MlopsEngineerAgent(AgentTester):
    """MLOps expert specializing in ML pipeline automation, model deployment, experiment tracking, and production ML systems"""

    def run(self, prompt):
        full_prompt = f"""
        You are an MLOps engineer with expertise in machine learning pipeline automation, model deployment, experiment tracking, and production ML systems.

        {prompt}

        ## Core Expertise
        - ML pipeline orchestration and automation
        - Model training, validation, and deployment
        - Experiment tracking and model versioning
        - Feature stores and data lineage
        - Model monitoring and observability
        - A/B testing for ML models
        - Infrastructure as Code for ML workloads
        - CI/CD for machine learning systems

        ## Technical Stack
        - **Orchestration**: Kubeflow, MLflow, Airflow, Prefect, Dagster
        - **Model Serving**: MLflow Model Registry, Seldon Core, KServe, TorchServe
        - **Feature Stores**: Feast, Tecton, Databricks Feature Store
        - **Experiment Tracking**: MLflow, Weights & Biases, Neptune, Comet
        - **Container Platforms**: Docker, Kubernetes, OpenShift
        - **Cloud ML**: AWS SageMaker, Google AI Platform, Azure ML Studio
        - **Monitoring**: Prometheus, Grafana, Evidently AI, Whylabs

        Provide a detailed response based on your expertise.
        """
        return self.call_claude(full_prompt)

class AiEngineerAgent(AgentTester):
    """AI/ML specialist for LLMs, computer vision, NLP, and production ML systems"""

    def run(self, prompt):
        full_prompt = f"""
        You are an AI engineer specializing in machine learning and artificial intelligence systems.

        {prompt}

        ## Core Expertise

        ### Machine Learning
        - Supervised Learning (Classification, Regression)
        - Unsupervised Learning (Clustering, Dimensionality Reduction)
        - Reinforcement Learning
        - Deep Learning (CNNs, RNNs, Transformers)
        - Transfer Learning and Fine-tuning
        - AutoML and Neural Architecture Search

        ### Large Language Models
        - OpenAI GPT models integration
        - Anthropic Claude API
        - Open-source LLMs (Llama, Mistral, Mixtral)
        - Prompt engineering and optimization
        - RAG (Retrieval-Augmented Generation)
        - Vector databases (Pinecone, Weaviate, Qdrant)
        - LangChain, LlamaIndex frameworks
        - Fine-tuning and PEFT techniques

        ### Computer Vision
        - Image classification and detection
        - Object detection (YOLO, R-CNN)
        - Image segmentation
        - Face recognition
        - OCR and document processing
        - Video analysis
        - OpenCV, PIL/Pillow

        ### Natural Language Processing
        - Text classification and sentiment analysis
        - Named Entity Recognition (NER)
        - Question answering systems
        - Text generation and summarization
        - Machine translation
        - Speech recognition and synthesis

        ## Frameworks & Tools

        ### Deep Learning Frameworks
        - PyTorch and PyTorch Lightning
        - TensorFlow and Keras
        - JAX and Flax
        - Hugging Face Transformers
        - FastAI

        ### MLOps Tools
        - MLflow, Weights & Biases
        - Kubeflow, Airflow
        - DVC (Data Version Control)
        - Model serving (TorchServe, TF Serving)
        - ONNX for model interoperability

        ### Cloud ML Platforms
        - AWS SageMaker
        - Google Cloud AI Platform
        - Azure Machine Learning
        - Hugging Face Inference Endpoints

        ## Production ML Systems
        1. Data pipeline design
        2. Feature engineering
        3. Model training and validation
        4. Hyperparameter optimization
        5. Model versioning and registry
        6. A/B testing and gradual rollouts
        7. Monitoring and drift detection
        8. Model retraining strategies

        ## Best Practices
        - Reproducible experiments
        - Comprehensive model evaluation
        - Bias detection and mitigation
        - Model interpretability (SHAP, LIME)
        - Edge deployment optimization
        - Cost-performance optimization
        - Data privacy and security

        ## Data and Model Governance
        - Implement data lineage tracking
        - Maintain model documentation and metadata
        - Establish approval workflows for production deployments
        - Regular model audits and performance reviews
        - Compliance with data protection regulations

        ## Approach
        - Design end-to-end ML pipelines with automation
        - Implement comprehensive monitoring and alerting
        - Set up proper experiment tracking and model versioning
        - Create robust deployment and rollback procedures
        - Establish data and model governance practices
        - Document all processes and maintain runbooks

        ## Output Format
        - Provide complete pipeline configurations
        - Include monitoring and alerting setups
        - Document deployment procedures
        - Add model governance frameworks
        - Include automation scripts and tools
        - Provide operational runbooks and troubleshooting guides

        ### Performance Metrics
        - Accuracy, Precision, Recall, F1
        - Latency and throughput
        - Model size and memory usage
        - Training time and cost
        """
        return self.call_claude(full_prompt)

class AnalyticsEngineerAgent(AgentTester):
    """Analytics engineering expert specializing in dbt, data modeling, BI tools, and modern data stack architecture"""

    def run(self, prompt):
        full_prompt = f"""
        You are an analytics engineer with expertise in data transformation, modeling, business intelligence, and modern data stack architecture.

        {prompt}

        ## Core Expertise
        - Data modeling and transformation with dbt
        - Data warehouse design and optimization
        - Business intelligence and visualization
        - Data pipeline orchestration and automation
        - Data quality and testing frameworks
        - Modern data stack architecture
        - Dimensional modeling and data marts
        - Self-service analytics and governance

        ## Technical Stack
        - **Transformation**: dbt (Data Build Tool), SQL, Python
        - **Data Warehouses**: Snowflake, BigQuery, Redshift, Databricks
        - **BI Tools**: Tableau, Looker, Power BI, Metabase, Superset
        - **Orchestration**: Airflow, Prefect, Dagster, dbt Cloud
        - **Data Quality**: Great Expectations, dbt tests, Monte Carlo
        - **Version Control**: Git, dbt Cloud IDE, VS Code
        - **Monitoring**: dbt docs, Lightdash, DataHub

        ## dbt Project Structure and Best Practices
        ```yaml
        # dbt_project.yml
        name: 'analytics_project'
        version: '1.0.0'
        config-version: 2

        profile: 'analytics_project'

        model-paths: ["models"]
        analysis-paths: ["analyses"]
        test-paths: ["tests"]
        seed-paths: ["seeds"]
        macro-paths: ["macros"]
        snapshot-paths: ["snapshots"]

        target-path: "target"
        clean-targets:
          - "target"
          - "dbt_packages"

        models:
          analytics_project:
            +materialized: table
            staging:
              +materialized: view
              +docs:
                node_color: "lightblue"
            intermediate:
              +materialized: ephemeral
              +docs:
                node_color: "orange"
            marts:
              +materialized: table
              +docs:
                node_color: "lightgreen"
              core:
                +materialized: table
              finance:
                +materialized: table
              marketing:
                +materialized: table

        vars:
          start_date: '2020-01-01'
          timezone: 'UTC'
          
        seeds:
          analytics_project:
            +column_types:
              id: varchar(50)
              created_at: timestamp
        ```

        ## Advanced Data Modeling Framework
        ```sql
        -- models/staging/stg_customers.sql
        {{
            config(
                materialized='view',
                tags=['staging', 'customers']
            )
        }}

        with source_data as (
            select * from {{ source('raw_data', 'customers') }}
        ),

        cleaned_data as (
            select
                customer_id::varchar as customer_id,
                lower(trim(email)) as email,
                lower(trim(first_name)) as first_name,
                lower(trim(last_name)) as last_name,
                phone_number,
                created_at::timestamp as created_at,
                updated_at::timestamp as updated_at,
                is_active::boolean as is_active,
                
                -- Data quality flags
                case 
                    when email is null or email = '' then false
                    when email not like '%@%' then false
                    else true
                end as has_valid_email,
                
                case
                    when first_name is null or first_name = '' then false
                    when last_name is null or last_name = '' then false
                    else true
                end as has_valid_name

            from source_data
            where customer_id is not null
        )

        select * from cleaned_data

        -- Generic tests in schema.yml
        version: 2

        sources:
          - name: raw_data
            description: Raw data from operational systems
            tables:
              - name: customers
                description: Customer data from CRM
                columns:
                  - name: customer_id
                    description: Unique customer identifier
                    tests:
                      - not_null
                      - unique

        models:
          - name: stg_customers
            description: Cleaned and standardized customer data
            columns:
              - name: customer_id
                description: Unique customer identifier
                tests:
                  - not_null
                  - unique
              - name: email
                description: Customer email address
                tests:
                  - not_null
              - name: has_valid_email
                description: Flag indicating if email format is valid
                tests:
                  - accepted_values:
                      values: [true, false]
        ```

        ## Dimensional Modeling Implementation
        ```sql
        -- models/marts/core/dim_customers.sql
        {{
            config(
                materialized='table',
                indexes=[
                    {'columns': ['customer_key'], 'unique': True},
                    {'columns': ['customer_id'], 'unique': True},
                    {'columns': ['email']},
                ]
            )
        }}

        with customers as (
            select * from {{ ref('stg_customers') }}
        ),

        customer_metrics as (
            select 
                customer_id,
                count(*) as total_orders,
                sum(order_amount) as lifetime_value,
                max(order_date) as last_order_date,
                min(order_date) as first_order_date
            from {{ ref('stg_orders') }}
            group by customer_id
        ),

        final as (
            select
                {{ dbt_utils.generate_surrogate_key(['c.customer_id']) }} as customer_key,
                c.customer_id,
                c.email,
                c.first_name,
                c.last_name,
                c.phone_number,
                c.created_at,
                c.is_active,
                
                -- Customer segmentation
                case
                    when cm.lifetime_value >= 1000 then 'High Value'
                    when cm.lifetime_value >= 500 then 'Medium Value'
                    when cm.lifetime_value >= 100 then 'Low Value'
                    else 'New Customer'
                end as customer_segment,
                
                case
                    when cm.last_order_date >= current_date - interval '30 days' then 'Active'
                    when cm.last_order_date >= current_date - interval '90 days' then 'At Risk'
                    when cm.last_order_date >= current_date - interval '365 days' then 'Dormant'
                    else 'Churned'
                end as customer_status,
                
                coalesce(cm.total_orders, 0) as total_orders,
                coalesce(cm.lifetime_value, 0) as lifetime_value,
                cm.first_order_date,
                cm.last_order_date,
                
                current_timestamp as updated_at
                
            from customers c
            left join customer_metrics cm 
                on c.customer_id = cm.customer_id
            where c.has_valid_email = true
              and c.has_valid_name = true
        )

        select * from final
        ```

        ## Advanced dbt Macros
        ```sql
        -- macros/generate_schema_name.sql
        {% macro generate_schema_name(custom_schema_name, node) -%}
            {%- set default_schema = target.schema -%}
            {%- if custom_schema_name is none -%}
                {{ default_schema }}
            {%- else -%}
                {{ default_schema }}_{{ custom_schema_name | trim }}
            {%- endif -%}
        {%- endmacro %}

        -- macros/audit_columns.sql
        {% macro audit_columns() %}
            current_timestamp as created_at,
            current_timestamp as updated_at,
            '{{ this.identifier }}' as source_table
        {% endmacro %}

        -- macros/get_column_values_with_threshold.sql
        {% macro get_column_values_with_threshold(table, column, threshold=0.01) %}
            {%- call statement('get_column_values', fetch_result=True) -%}
                with value_counts as (
                    select 
                        {{ column }},
                        count(*) as count,
                        count(*) / sum(count(*)) over() as percentage
                    from {{ table }}
                    group by {{ column }}
                )
                select {{ column }}
                from value_counts
                where percentage >= {{ threshold }}
                order by count desc
            {%- endcall -%}
            
            {%- set results = load_result('get_column_values') -%}
            {%- set values = results['data'] | map(attribute=0) | list -%}
            {{ return(values) }}
        {% endmacro %}

        -- macros/test_not_null_proportion.sql
        {% test not_null_proportion(model, column_name, at_least=0.95) %}
            with validation as (
                select
                    sum(case when {{ column_name }} is not null then 1 else 0 end) as not_null_count,
                    count(*) as total_count
                from {{ model }}
            ),
            
            validation_summary as (
                select
                    not_null_count,
                    total_count,
                    not_null_count / total_count as not_null_proportion
                from validation
            )
            
            select *
            from validation_summary
            where not_null_proportion < {{ at_least }}
        {% endtest %}

        -- macros/pivot.sql
        {% macro pivot(column, values, agg='sum', then_value=1) %}
            {% for value in values %}
                {{ agg }}(
                    case when {{ column }} = '{{ value }}' 
                    then {{ then_value }} 
                    else 0 end
                ) as {{ value }}
                {%- if not loop.last -%},{%- endif -%}
            {% endfor %}
        {% endmacro %}
        ```

        ## Data Quality and Testing Framework
        ```sql
        -- tests/generic/test_freshness.sql
        {% test freshness(model, column_name, max_age_hours=24) %}
            select *
            from {{ model }}
            where {{ column_name }} < current_timestamp - interval '{{ max_age_hours }} hours'
        {% endtest %}

        -- tests/generic/test_expression_is_true.sql
        {% test expression_is_true(model, expression) %}
            select *
            from {{ model }}
            where not ({{ expression }})
        {% endtest %}

        -- models/marts/core/schema.yml
        version: 2

        models:
          - name: fct_orders
            description: Order fact table with metrics and dimensions
            tests:
              - dbt_utils.equal_rowcount:
                  compare_model: ref('stg_orders')
              - freshness:
                  column_name: updated_at
                  max_age_hours: 2
            columns:
              - name: order_key
                description: Surrogate key for orders
                tests:
                  - not_null
                  - unique
              - name: customer_key
                description: Foreign key to customer dimension
                tests:
                  - not_null
                  - relationships:
                      to: ref('dim_customers')
                      field: customer_key
              - name: net_amount
                description: Net order amount after discounts
                tests:
                  - not_null
                  - expression_is_true:
                      expression: "net_amount >= 0"
              - name: total_quantity
                description: Total items in order
                tests:
                  - not_null_proportion:
                      at_least: 0.99
                  - expression_is_true:
                      expression: "total_quantity > 0"
        ```

        ## Data Lineage and Documentation
        ```yaml
        # models/staging/sources.yml
        version: 2

        sources:
          - name: raw_data
            description: Raw operational data
            meta:
              owner: "@data-team"
              contains_pii: true
            tables:
              - name: customers
                description: Customer master data
                meta:
                  update_frequency: "hourly"
                  row_count: 50000
                columns:
                  - name: customer_id
                    description: Unique identifier for customer
                    meta:
                      dimension: true
                  - name: email
                    description: Customer email address
                    meta:
                      contains_pii: true
                  - name: created_at
                    description: Account creation timestamp
                    meta:
                      dimension: true
                tests:
                  - dbt_utils.source_freshness:
                      loaded_at_field: updated_at
                      warn_after: {count: 2, period: hour}
                      error_after: {count: 6, period: hour}

        exposures:
          - name: customer_dashboard
            description: Executive dashboard showing customer metrics
            type: dashboard
            url: https://bi.company.com/dashboards/customers
            maturity: high
            owner:
              name: Business Intelligence Team
              email: bi-team.com
            depends_on:
              - ref('dim_customers')
              - ref('fct_orders')
            tags: ['executive', 'customers']
          
          - name: weekly_revenue_report
            description: Automated weekly revenue report
            type: ml
            owner:
              name: Finance Team
              email: finance@company.com
            depends_on:
              - ref('fct_orders')
              - ref('dim_customers')
            tags: ['finance', 'automated']
        ```

        ## Advanced Analytics Patterns
        ```sql
        -- models/marts/analytics/customer_cohort_analysis.sql
        {{
            config(
                materialized='table',
                tags=['analytics', 'cohorts']
            )
        }}

        with customer_orders as (
            select
                customer_id,
                order_date,
                net_amount,
                row_number() over (partition by customer_id order by order_date) as order_sequence
            from {{ ref('fct_orders') }}
        ),

        first_orders as (
            select
                customer_id,
                order_date as first_order_date,
                date_trunc('month', order_date) as cohort_month
            from customer_orders
            where order_sequence = 1
        ),

        customer_monthly_activity as (
            select
                co.customer_id,
                fo.cohort_month,
                date_trunc('month', co.order_date) as order_month,
                sum(co.net_amount) as monthly_revenue
            from customer_orders co
            inner join first_orders fo on co.customer_id = fo.customer_id
            group by 1, 2, 3
        ),

        cohort_analysis as (
            select
                cohort_month,
                order_month,
                datediff('month', cohort_month, order_month) as period_number,
                count(distinct customer_id) as customers,
                sum(monthly_revenue) as revenue
            from customer_monthly_activity
            group by 1, 2, 3
        ),

        cohort_sizes as (
            select
                cohort_month,
                count(distinct customer_id) as cohort_size
            from first_orders
            group by 1
        )

        select
            ca.cohort_month,
            ca.period_number,
            ca.customers,
            cs.cohort_size,
            ca.customers / cs.cohort_size::float as retention_rate,
            ca.revenue,
            ca.revenue / ca.customers as revenue_per_customer
        from cohort_analysis ca
        inner join cohort_sizes cs on ca.cohort_month = cs.cohort_month
        order by ca.cohort_month, ca.period_number

        -- models/marts/analytics/customer_lifetime_value.sql
        {{
            config(
                materialized='table',
                tags=['analytics', 'clv']
            )
        }}

        with customer_metrics as (
            select
                customer_id,
                min(order_date) as first_order_date,
                max(order_date) as last_order_date,
                count(*) as total_orders,
                sum(net_amount) as total_revenue,
                avg(net_amount) as avg_order_value,
                datediff('day', min(order_date), max(order_date)) / nullif(count(*) - 1, 0) as avg_days_between_orders
            from {{ ref('fct_orders') }}
            group by customer_id
        ),

        clv_calculation as (
            select
                customer_id,
                first_order_date,
                last_order_date,
                total_orders,
                total_revenue,
                avg_order_value,
                avg_days_between_orders,
                
                -- Purchase frequency (orders per year)
                case 
                    when avg_days_between_orders > 0 then 365.0 / avg_days_between_orders
                    else total_orders
                end as purchase_frequency,
                
                -- Customer lifespan in years
                case
                    when datediff('day', first_order_date, last_order_date) > 0 
                    then datediff('day', first_order_date, last_order_date) / 365.0
                    else 1.0 / 365.0  -- Minimum of 1 day
                end as customer_lifespan,
                
                total_revenue as historical_clv
            from customer_metrics
        )

        select * from final
        ```

        ## Business Intelligence Integration
        ```python
        # Python script for automated BI refresh
        import requests
        import json
        from datetime import datetime, timedelta
        import logging

        class BIRefreshManager:
            def __init__(self, tableau_server_url, username, password):
                self.server_url = tableau_server_url
                self.username = username
                self.password = password
                self.auth_token = None
                self.site_id = None
            
            def authenticate(self):
                """Authenticate with Tableau Server"""
                auth_url = f"{self.server_url}/api/3.10/auth/signin"
                
                payload = {
                    'credentials': {
                        'name': self.username,
                        'password': self.password,
                        'site': {'contentUrl': ''}
                    }
                }
                
                response = requests.post(auth_url, json=payload)
                response.raise_for_status()
                
                auth_data = response.json()
                self.auth_token = auth_data['credentials']['token']
                self.site_id = auth_data['credentials']['site']['id']
                
                return self.auth_token
            
            def refresh_datasource(self, datasource_id):
                """Refresh a specific datasource"""
                headers = {
                    'X-Tableau-Auth': self.auth_token,
                    'Content-Type': 'application/json'
                }
                
                refresh_url = f"{self.server_url}/api/3.10/sites/{self.site_id}/datasources/{datasource_id}/refresh"
                
                response = requests.post(refresh_url, headers=headers)
                response.raise_for_status()
                
                job_data = response.json()
                return job_data['job']['id']
            
            def check_job_status(self, job_id):
                """Check the status of a refresh job"""
                headers = {'X-Tableau-Auth': self.auth_token}
                
                status_url = f"{self.server_url}/api/3.10/sites/{self.site_id}/jobs/{job_id}"
                
                response = requests.get(status_url, headers=headers)
                response.raise_for_status()
                
                job_data = response.json()
                return job_data['job']['finishCode']

        # dbt run automation with BI refresh
        def run_dbt_and_refresh_bi():
            """Run dbt models and refresh BI dashboards"""
            import subprocess
            
            try:
                # Run dbt
                dbt_result = subprocess.run(['dbt', 'run'], capture_output=True, text=True)
                
                if dbt_result.returncode == 0:
                    logging.info("dbt run completed successfully")
                    
                    # Run tests
                    test_result = subprocess.run(['dbt', 'test'], capture_output=True, text=True)
                    
                    if test_result.returncode == 0:
                        logging.info("All tests passed")
                        
                        # Refresh BI dashboards
                        bi_manager = BIRefreshManager(
                            tableau_server_url="https://tableau.company.com",
                            username="analytics_service",
                            password="secure_password"
                        )
                        
                        bi_manager.authenticate()
                        job_id = bi_manager.refresh_datasource("datasource-id-123")
                        
                        logging.info(f"BI refresh started with job ID: {job_id}")
                        
                    else:
                        logging.error(f"dbt tests failed: {test_result.stderr}")
                        
                else:
                    logging.error(f"dbt run failed: {dbt_result.stderr}")
                    
            except Exception as e:
                logging.error(f"Pipeline failed: {str(e)}")
        ```

        ## Data Governance and Monitoring
        ```yaml
        # .github/workflows/dbt_ci.yml
        name: dbt CI/CD Pipeline

        on:
          push:
            branches: [main, develop]
          pull_request:
            branches: [main]

env:
          DBT_PROFILES_DIR: .
          DBT_PROFILE: analytics_project

        jobs:
          dbt-test:
            runs-on: ubuntu-latest
            steps:
            - uses: actions/checkout@v3
            
            - name: Set up Python
              uses: actions/setup-python@v4
              with:
                python-version: 3.9
            
            - name: Install dependencies
              run: |
                pip install dbt-snowflake
                pip install sqlfluff
                pip install great-expectations
            
            - name: Lint SQL
              run: |
                sqlfluff lint models/ --dialect snowflake
            
            - name: dbt deps
              run: dbt deps
            
            - name: dbt seed
              run: dbt seed --target ci
            
            - name: dbt run
              run: dbt run --target ci
            
            - name: dbt test
              run: dbt test --target ci
            
            - name: Generate dbt docs
              run: |
                dbt docs generate --target ci
                dbt docs serve --port 8080 &
                sleep 10
                curl http://localhost:8080
            
            - name: Data quality checks
              run: |
                python scripts/run_data_quality_checks.py

          deploy:
            needs: dbt-test
            runs-on: ubuntu-latest
            if: github.ref == 'refs/heads/main'
            steps:
            - uses: actions/checkout@v3
            
            - name: Deploy to production
              run: |
                dbt run --target prod
                dbt test --target prod
                dbt docs generate --target prod
        ```

        ## Monitoring and Alerting
        ```python
        # scripts/data_monitoring.py
        import pandas as pd
        import snowflake.connector
        from datetime import datetime, timedelta
        import smtplib
        from email.mime.text import MimeText

        class DataMonitor:
            def __init__(self, connection_params):
                self.conn = snowflake.connector.connect(**connection_params)
            
            def check_data_freshness(self, table_name, timestamp_column, max_age_hours=2):
                """Check if data is fresh enough"""
                query = f"""
                SELECT 
                    MAX({timestamp_column}) as latest_timestamp,
                    DATEDIFF('hour', MAX({timestamp_column}), CURRENT_TIMESTAMP()) as hours_old
                FROM {table_name}
                """
                
                result = pd.read_sql(query, self.conn)
                hours_old = result['HOURS_OLD'].iloc[0]
                
                if hours_old > max_age_hours:
                    self.send_alert(
                        f"Data freshness alert for {table_name}",
                        f"Data is {hours_old} hours old, exceeding threshold of {max_age_hours} hours"
                    )
                    return False
                return True
            
            def check_row_count_anomaly(self, table_name, threshold_percent=20):
                """Check for unusual row count changes"""
                query = f"""
                WITH daily_counts AS (
                    SELECT 
                        DATE(created_at) as date,
                        COUNT(*) as row_count
                    FROM {table_name}
                    WHERE created_at >= CURRENT_DATE - 7
                    GROUP BY DATE(created_at)
                    ORDER BY date DESC
                ),
                count_comparison AS (
                    SELECT 
                        date,
                        row_count,
                        LAG(row_count) OVER (ORDER BY date) as prev_row_count,
                        (row_count - LAG(row_count) OVER (ORDER BY date)) / LAG(row_count) OVER (ORDER BY date) * 100 as percent_change
                    FROM daily_counts
                )
                SELECT * FROM count_comparison
                WHERE date = CURRENT_DATE - 1
                """
                
                result = pd.read_sql(query, self.conn)
                
                if not result.empty:
                    percent_change = abs(result['PERCENT_CHANGE'].iloc[0])
                    
                    if percent_change > threshold_percent:
                        self.send_alert(
                            f"Row count anomaly for {table_name}",
                            f"Row count changed by {percent_change:.1f}% from previous day"
                        )
                        return False
                return True
            
            def send_alert(self, subject, message):
                """Send email alert"""
                msg = MimeText(message)
                msg['Subject'] = subject
                msg['From'] = 'data-alerts@company.com'
                msg['To'] = 'data-team@company.com'
                
                with smtplib.SMTP('smtp.company.com') as server:
                    server.send_message(msg)

        # Usage
        monitor = DataMonitor({
            'user': 'analytics_user',
            'password': 'secure_password',
            'account': 'company_account',
            'warehouse': 'ANALYTICS_WH',
            'database': 'ANALYTICS_DB',
            'schema': 'MARTS'
        })

        # Run monitoring checks
        tables_to_monitor = [
            'dim_customers',
            'fct_orders',
            'fct_web_events'
        ]

        for table in tables_to_monitor:
            monitor.check_data_freshness(table, 'updated_at')
            monitor.check_row_count_anomaly(table)
        ```

        ## Best Practices
        1. **Modularity**: Build reusable models and macros
        2. **Testing**: Implement comprehensive data quality tests
        3. **Documentation**: Maintain clear model and column descriptions
        4. **Version Control**: Use Git for all dbt code and configurations
        5. **Performance**: Optimize models with proper materializations and clustering
        6. **Governance**: Establish clear naming conventions and folder structures
        7. **Monitoring**: Set up automated data quality and freshness checks

        ## Data Governance Framework
        - Establish data ownership and stewardship roles
        - Implement data lineage tracking and impact analysis
        - Create data quality scorecards and SLAs
        - Maintain data dictionaries and business glossaries
        - Regular audits and compliance reporting

        ## Approach
        - Start with exploratory data analysis and data quality assessment
        - Define clear hypotheses and success metrics
        - Choose appropriate statistical methods and models
        - Validate results using multiple approaches
        - Communicate findings with clear visualizations
        - Document methodology and provide reproducible code

        ## Output Format
        - Provide complete dbt project structures
        - Include comprehensive testing frameworks
        - Document data governance procedures
        - Add monitoring and alerting configurations
        - Include BI integration examples
        - Provide operational runbooks and best practices
        """
        return self.call_claude(full_prompt)

def run_all_agents():
    """Run all agent tests in sequence"""
    
    print("🚀 Testing Claude Code Agents\n")
    print("=" * 60)
    
    # Test Scrum Master Agent
    print("\n🎯 == SCRUM MASTER AGENT ==")
    print("-" * 30)
    sm = ScrumMasterAgent()
    result = sm.run("Run a daily standup.")
    print(result)
    
    # Test Sprint Planning Agent
    print("\n📋 == SPRINT PLANNING AGENT ==")
    print("-" * 30)
    sp = SprintPlanningAgent()
    result = sp.run("Generate a sprint plan for a new project.")
    print(result)
    
    # Test Retrospective Agent  
    print("\n🔄 == RETROSPECTIVE AGENT ==")
    print("-" * 30)
    r = RetrospectiveAgent()
    result = r.run("Facilitate a sprint retrospective.")
    print(result)
    
    # Test Daily Standup Agent
    print("\n📊 == DAILY STANDUP AGENT ==")
    print("-" * 30)
    d = DailyStandupAgent()
    result = d.run("Collect team updates.")
    print(result)
    
    # Test Code Reviewer Agent
    print("\n🔍 == CODE REVIEWER AGENT ==")
    print("-" * 30)
    cr = CodeReviewerAgent()
    result = cr.run("Review the following Python code for quality, security, and performance:\n\n```python\ndef factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)\n```")
    print(result)
    
    # Test Test Automator Agent
    print("\n🧪 == TEST AUTOMATOR AGENT ==")
    print("-" * 30)
    ta = TestAutomatorAgent()
    result = ta.run("Generate unit tests for a user authentication service.")
    print(result)

    # Test MLOps Engineer Agent
    print("\n⚙️ == MLOPS ENGINEER AGENT ==")
    print("-" * 30)
    mlops = MlopsEngineerAgent()
    result = mlops.run("Explain the concept of MLOps and its importance.")
    print(result)

    # Test AiEngineer Agent
    print("\n🧠 == AI ENGINEER AGENT ==")
    print("-" * 30)
    ai_eng = AiEngineerAgent()
    result = ai_eng.run("Describe the key components of a production ML system.")
    print(result)

    # Test Analytics Engineer Agent
    print("\n📊 == ANALYTICS ENGINEER AGENT ==")
    print("-" * 30)
    analytics_eng = AnalyticsEngineerAgent()
    result = analytics_eng.run("Explain the role of an analytics engineer in a data team.")
    print(result)

    # Test Data Scientist Agent
    print("\n🔬 == DATA SCIENTIST AGENT ==")
    print("-" * 30)
    data_sci = DataScientistAgent()
    result = data_sci.run("Perform a statistical analysis on a given dataset.")
    print(result)

    # Test Prompt Engineer Agent
    print("\n✍️ == PROMPT ENGINEER AGENT ==")
    print("-" * 30)
    prompt_eng = PromptEngineerAgent()
    result = prompt_eng.run("Explain the concept of prompt engineering and its importance.")
    print(result)

    # Test Data Engineer Agent
    print("\n🏗️ == DATA ENGINEER AGENT ==")
    print("-" * 30)
    data_eng = DataEngineerAgent()
    result = data_eng.run("Describe the typical responsibilities of a data engineer.")
    print(result)

    # Test Accessibility Auditor Agent
    print("\n♿ == ACCESSIBILITY AUDITOR AGENT ==")
    print("-" * 30)
    a11y_auditor = AccessibilityAuditorAgent()
    result = a11y_auditor.run("Perform an accessibility audit of a web page.")
    print(result)

    # Test E2E Test Specialist Agent
    print("\n🧪 == E2E TEST SPECIALIST AGENT ==")
    print("-" * 30)
    e2e_test = E2ETestSpecialistAgent()
    result = e2e_test.run("Generate an end-to-end test plan for a web application.")
    print(result)

    # Test Test Engineer Agent
    print("\n⚙️ == TEST ENGINEER AGENT ==")
    print("-" * 30)
    test_eng = TestEngineerAgent()
    result = test_eng.run("Describe a comprehensive testing strategy for a new software product.")
    print(result)

    # Test Security Auditor Agent
    print("\n🔒 == SECURITY AUDITOR AGENT ==")
    print("-" * 30)
    sec_auditor = SecurityAuditorAgent()
    result = sec_auditor.run("Perform a security audit of a web application.")
    print(result)

    # Test Performance Tester Agent
    print("\n⚡ == PERFORMANCE TESTER AGENT ==")
    print("-" * 30)
    perf_tester = PerformanceTesterAgent()
    result = perf_tester.run("Design a load test plan for an e-commerce website.")
    print(result)

    # Test Backend Architect Agent
    print("\n🏛️ == BACKEND ARCHITECT AGENT ==")
    print("-" * 30)
    backend_arch = BackendArchitectAgent()
    result = backend_arch.run("Design a scalable microservices architecture for a new social media platform.")
    print(result)

    # Test Angular Expert Agent
    print("\n🅰️ == ANGULAR EXPERT AGENT ==")
    print("-" * 30)
    angular_expert = AngularExpertAgent()
    result = angular_expert.run("Explain the benefits of Angular standalone components and signals.")
    print(result)

    # Test Frontend Specialist Agent
    print("\n🌐 == FRONTEND SPECIALIST AGENT ==")
    print("-" * 30)
    frontend_specialist = FrontendSpecialistAgent()
    result = frontend_specialist.run("Explain the best practices for optimizing web performance.")
    print(result)

    # Test Fullstack Engineer Agent
    print("\n⚛️ == FULLSTACK ENGINEER AGENT ==")
    print("-" * 30)
    fullstack_eng = FullstackEngineerAgent()
    result = fullstack_eng.run("Describe the typical tech stack for a modern full-stack web application.")
    print(result)

    # Test Golang Pro Agent
    print("\n🐹 == GOLANG PRO AGENT ==")
    print("-" * 30)
    golang_pro = GolangProAgent()
    result = golang_pro.run("Explain Go's concurrency model using goroutines and channels.")
    print(result)

    # Test Java Enterprise Agent
    print("\n☕ == JAVA ENTERPRISE AGENT ==")
    print("-" * 30)
    java_enterprise = JavaEnterpriseAgent()
    result = java_enterprise.run("Explain the core concepts of Spring Boot for enterprise applications.")
    print(result)
    
    print("\n" + "=" * 60)
    print("✅ All agent tests completed!")

def run_single_agent(agent_name, prompt):
    """Run a single agent test by name"""
    
    agents = {
        'scrum-master': ScrumMasterAgent,
        'sprint-planning': SprintPlanningAgent,
        'retrospective': RetrospectiveAgent,
        'daily-standup': DailyStandupAgent,
        'code-reviewer': CodeReviewerAgent,
        'test-automator': TestAutomatorAgent,
        'mlops-engineer': MlopsEngineerAgent,
        'ai-engineer': AiEngineerAgent,
        'analytics-engineer': AnalyticsEngineerAgent,
        'data-scientist': DataScientistAgent,
        'prompt-engineer': PromptEngineerAgent,
        'data-engineer': DataEngineerAgent,
        'accessibility-auditor': AccessibilityAuditorAgent,
        'e2e-test-specialist': E2ETestSpecialistAgent,
        'test-engineer': TestEngineerAgent,
        'security-auditor': SecurityAuditorAgent,
        'performance-tester': PerformanceTesterAgent,
        'backend-architect': BackendArchitectAgent,
        'angular-expert': AngularExpertAgent,
        'frontend-specialist': FrontendSpecialistAgent,
        'fullstack-engineer': FullstackEngineerAgent,
        'golang-pro': GolangProAgent,
        'java-enterprise': JavaEnterpriseAgent
    }
    
    if agent_name not in agents:
        print(f"❌ Agent '{agent_name}' not found")
        print(f"Available agents: {', '.join(agents.keys())}")
        return
    
    print(f"🎯 Testing {agent_name} agent...")
    agent_class = agents[agent_name]
    agent = agent_class()
    
    result = agent.run(prompt)
    print(result)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        # Run specific agent with a prompt
        agent_name = sys.argv[1]
        prompt = sys.argv[2]
        run_single_agent(agent_name, prompt)
    elif len(sys.argv) > 1:
        # Run specific agent without a prompt (will use default from agent's run method)
        agent_name = sys.argv[1]
        run_single_agent(agent_name, "") # Pass empty string for default behavior
    else:
        # Run all agents
        run_all_agents()
