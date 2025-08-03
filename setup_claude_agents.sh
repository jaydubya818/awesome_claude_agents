#!/bin/bash

echo "🚀 Setting up Claude Code with 108 Specialized Sub-Agents..."

# Create .claude directory structure
mkdir -p .claude/agents
mkdir -p .claude/config

echo "📁 Created directory structure"

# Copy all agents to .claude/agents
echo "📋 Copying agents..."
cp -r orchestration .claude/agents/
cp -r development .claude/agents/
cp -r design .claude/agents/
cp -r quality .claude/agents/
cp -r security .claude/agents/
cp -r data-ai .claude/agents/
cp -r devops .claude/agents/
cp -r documentation .claude/agents/
cp -r product .claude/agents/
cp -r marketing .claude/agents/
cp -r operations .claude/agents/
cp -r specialized .claude/agents/

echo "✅ All agents copied to .claude/agents/"

# Create agent index
cat > .claude/agents/index.md << 'EOF'
# Claude Code Sub-Agent Index

## 🎯 Orchestration & Management (5 agents)
- agent-organizer
- context-manager
- project-analyst
- team-configurator
- tech-lead-orchestrator

## 🏗️ Development & Architecture (24 agents)
- ai-engineer
- api-architect
- api-developer
- backend-architect
- backend-developer
- code-archaeologist
- electorn-pro
- frontend-developer
- full-stack-developer
- golang-pro
- graphql-architect
- legacy-modernizer
- mobile-app-builder
- mobile-developer
- nextjs-pro
- python-pro
- rapid-prototyper
- react-component-architect
- react-nextjs-expert
- react-pro
- refactor
- shadcn-ui-builder
- typescript-pro
- vue-component-architect
- vue-nuxt-expert
- vue-state-manager

## 🎨 Design & UX (7 agents)
- brand-guardian
- dx-optimizer
- ui-designer
- ux-designer
- ux-researcher
- visual-storyteller
- whimsy-injector

## 🔧 Quality Assurance & Testing (15 agents)
- api-tester
- architect-review
- best-practices
- code-reviewer
- database-optimizer
- performance-benchmarker
- performance-engineer
- performance-optimizer
- postgres-pro
- qa-expert
- tdd-specialist
- test-automator
- test-results-analyzer
- test-runner
- test-writer-fixer

## 🔒 Security & Compliance (4 agents)
- devops-incident-responder
- incident-responder
- security-auditor
- security-scanner

## 📊 Data & AI (4 agents)
- data-engineer
- data-scientist
- ml-engineer
- prompt-engineer

## 🚀 DevOps & Infrastructure (13 agents)
- cloud-architect
- deployment-engineer
- devops-automator
- devops-engineer
- django-api-developer
- django-backend-expert
- django-orm-expert
- infrastructure-maintainer
- laravel-backend-expert
- laravel-eloquent-expert
- rails-activerecord-expert
- rails-api-developer
- rails-backend-expert

## 📝 Documentation & Communication (6 agents)
- api-documenter
- content-creator
- debugger
- doc-writer
- documentation-expert
- documentation-specialist

## 🎯 Product & Business (9 agents)
- ai-scrum-master
- experiment-tracker
- feedback-synthesizer
- product-manager
- project-planner
- project-shipper
- sprint-prioritizer
- studio-producer
- trend-researcher

## 📈 Marketing & Growth (7 agents)
- app-store-optimizer
- growth-hacker
- instagram-curator
- marketing-writer
- reddit-community-builder
- tiktok-strategist
- twitter-engager

## 🏢 Operations (5 agents)
- analytics-reporter
- finance-tracker
- infrastructure-maintainer
- legal-compliance-checker
- support-responder

## 🎭 Specialized & Utility (9 agents)
- creating-agents
- dependencies
- joker-bonus
- joker
- studio-coach-bonus
- studio-coach
- tailwind-css-expert
- tool-evaluator
- workflow-optimizer

Total: 108 specialized sub-agents
EOF

echo "📝 Created agent index"

# Create Claude Code configuration
cat > .claude/config.json << 'EOF'
{
  "project": {
    "name": "Comprehensive Sub-Agent Collection",
    "description": "108 specialized AI sub-agents for Claude Code workflows",
    "version": "1.0.0"
  },
  "agents": {
    "directory": ".claude/agents",
    "index_file": ".claude/agents/index.md",
    "auto_discovery": true,
    "categories": [
      "orchestration",
      "development", 
      "design",
      "quality",
      "security",
      "data-ai",
      "devops",
      "documentation",
      "product",
      "marketing",
      "operations",
      "specialized"
    ]
  },
  "workflows": {
    "default_orchestrator": "supervisor-orchestrator",
    "auto_delegation": true,
    "quality_gates": true
  }
}
EOF

echo "⚙️ Created Claude Code configuration"

# Create agent discovery script
cat > .claude/discover_agents.sh << 'EOF'
#!/bin/bash

echo "🔍 Discovering Claude Code Sub-Agents..."

# Find all agent files
AGENT_FILES=$(find .claude/agents -name "*.md" -type f | grep -v "index.md")

echo "📊 Found $(echo "$AGENT_FILES" | wc -l) agents:"
echo

# Display agents by category
for category in orchestration development design quality security data-ai devops documentation product marketing operations specialized; do
    if [ -d ".claude/agents/$category" ]; then
        count=$(ls -1 ".claude/agents/$category"/*.md 2>/dev/null | wc -l)
        echo "📁 $category: $count agents"
    fi
done

echo
echo "✅ Agent discovery complete!"
echo "🎯 Ready to use with Claude Code"
EOF

chmod +x .claude/discover_agents.sh

# Create validation script
cat > .claude/validate_agents.sh << 'EOF'
#!/bin/bash

echo "🔍 Validating Claude Code Sub-Agents..."

# Check if all required directories exist
REQUIRED_DIRS=("orchestration" "development" "design" "quality" "security" "data-ai" "devops" "documentation" "product" "marketing" "operations" "specialized")

for dir in "${REQUIRED_DIRS[@]}"; do
    if [ -d ".claude/agents/$dir" ]; then
        count=$(ls -1 ".claude/agents/$dir"/*.md 2>/dev/null | wc -l)
        echo "✅ $dir: $count agents"
    else
        echo "❌ $dir: Missing directory"
    fi
done

# Check for required files
REQUIRED_FILES=("supervisor-orchestrator.md" "agent-organizer.md" "code-reviewer.md" "test-automator.md")

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f ".claude/agents/orchestration/$file" ] || [ -f ".claude/agents/quality/$file" ]; then
        echo "✅ $file: Found"
    else
        echo "❌ $file: Missing"
    fi
done

# Count total agents
TOTAL_AGENTS=$(find .claude/agents -name "*.md" -type f | grep -v "index.md" | wc -l)
echo
echo "📊 Total agents found: $TOTAL_AGENTS"
echo "🎯 Expected: 108"

if [ "$TOTAL_AGENTS" -eq 108 ]; then
    echo "✅ Validation successful!"
else
    echo "⚠️  Validation incomplete - some agents may be missing"
fi
EOF

chmod +x .claude/validate_agents.sh

# Create usage examples
cat > .claude/examples.md << 'EOF'
# 🚀 Claude Code Sub-Agent Usage Examples

## 🎯 Quick Start Examples

### Example 1: React App Development
```
@supervisor-orchestrator Build a React e-commerce app with payment integration
```

### Example 2: Business App Launch
```
@supervisor-orchestrator Launch a meditation app with marketing strategy
```

### Example 3: Legacy System Modernization
```
@supervisor-orchestrator Modernize a legacy PHP system to Laravel
```

### Example 4: Sprint Management
```
@ai-scrum-master Set up automated scrum management for the development team
```

### Example 5: Code Review
```
@code-reviewer Review this React component for best practices
```

## 🔧 Agent Selection Patterns

### Development Workflows
- **Frontend**: `frontend-developer` + `ui-designer` + `test-automator`
- **Backend**: `backend-architect` + `api-developer` + `database-optimizer`
- **Full-Stack**: `full-stack-developer` + `devops-automator` + `code-reviewer`

### Quality Assurance
- **Testing**: `test-automator` + `test-writer-fixer` + `qa-expert`
- **Performance**: `performance-engineer` + `performance-benchmarker`
- **Security**: `security-auditor` + `security-scanner`

### Business Operations
- **Product**: `product-manager` + `feedback-synthesizer` + `trend-researcher`
- **Marketing**: `growth-hacker` + `content-creator` + platform specialists
- **Operations**: `analytics-reporter` + `finance-tracker` + `support-responder`

## 🎯 Best Practices

1. **Start with Orchestrator**: Use `supervisor-orchestrator` for complex projects
2. **Quality Gates**: Always include `code-reviewer` for code quality
3. **Specialized Agents**: Use framework-specific agents when available
4. **Auto-Delegation**: Trust Claude Code to select optimal agents
5. **Context Management**: Provide rich context for better agent selection
EOF

echo "📚 Created usage examples"

# Create categories configuration
cat > .claude/categories.json << 'EOF'
{
  "orchestration": {
    "description": "Master coordination and team management",
    "primary_agent": "supervisor-orchestrator",
    "agents": ["agent-organizer", "context-manager", "project-analyst", "team-configurator", "tech-lead-orchestrator"]
  },
  "development": {
    "description": "Software development and architecture",
    "primary_agent": "full-stack-developer",
    "agents": ["backend-architect", "frontend-developer", "api-architect", "react-pro", "vue-component-architect", "python-pro", "golang-pro", "typescript-pro", "mobile-developer", "ai-engineer", "rapid-prototyper", "legacy-modernizer", "code-archaeologist", "refactor", "electorn-pro", "nextjs-pro", "graphql-architect", "shadcn-ui-builder", "vue-nuxt-expert", "vue-state-manager", "react-component-architect", "react-nextjs-expert", "mobile-app-builder", "api-developer"]
  },
  "design": {
    "description": "User experience and visual design",
    "primary_agent": "ui-designer",
    "agents": ["ux-designer", "ux-researcher", "visual-storyteller", "brand-guardian", "whimsy-injector", "dx-optimizer"]
  },
  "quality": {
    "description": "Testing, review, and quality assurance",
    "primary_agent": "code-reviewer",
    "agents": ["test-automator", "test-writer-fixer", "api-tester", "performance-benchmarker", "test-results-analyzer", "qa-expert", "architect-review", "best-practices", "performance-engineer", "performance-optimizer", "database-optimizer", "postgres-pro", "tdd-specialist", "test-runner"]
  },
  "security": {
    "description": "Security auditing and incident response",
    "primary_agent": "security-auditor",
    "agents": ["incident-responder", "devops-incident-responder", "security-scanner"]
  },
  "data-ai": {
    "description": "Data science and AI/ML engineering",
    "primary_agent": "ai-engineer",
    "agents": ["ml-engineer", "prompt-engineer", "data-scientist", "data-engineer"]
  },
  "devops": {
    "description": "DevOps and infrastructure management",
    "primary_agent": "devops-automator",
    "agents": ["deployment-engineer", "cloud-architect", "infrastructure-maintainer", "devops-engineer", "laravel-backend-expert", "laravel-eloquent-expert", "django-backend-expert", "django-api-developer", "django-orm-expert", "rails-backend-expert", "rails-api-developer", "rails-activerecord-expert"]
  },
  "documentation": {
    "description": "Documentation and communication",
    "primary_agent": "documentation-expert",
    "agents": ["api-documenter", "documentation-specialist", "content-creator", "doc-writer", "debugger"]
  },
  "product": {
    "description": "Product management and business strategy",
    "primary_agent": "product-manager",
    "agents": ["ai-scrum-master", "feedback-synthesizer", "sprint-prioritizer", "trend-researcher", "experiment-tracker", "project-planner", "project-shipper", "studio-producer"]
  },
  "marketing": {
    "description": "Marketing and growth strategies",
    "primary_agent": "growth-hacker",
    "agents": ["app-store-optimizer", "instagram-curator", "reddit-community-builder", "tiktok-strategist", "twitter-engager", "marketing-writer"]
  },
  "operations": {
    "description": "Business operations and analytics",
    "primary_agent": "analytics-reporter",
    "agents": ["finance-tracker", "infrastructure-maintainer", "legal-compliance-checker", "support-responder"]
  },
  "specialized": {
    "description": "Specialized utilities and tools",
    "primary_agent": "workflow-optimizer",
    "agents": ["creating-agents", "dependencies", "joker", "joker-bonus", "studio-coach", "studio-coach-bonus", "tailwind-css-expert", "tool-evaluator"]
  }
}
EOF

echo "📋 Created categories configuration"

# Run validation
echo "🔍 Running validation..."
./.claude/validate_agents.sh

echo
echo "🎉 Setup Complete!"
echo
echo "📋 Available Commands:"
echo "  ./.claude/discover_agents.sh - Discover all agents"
echo "  ./.claude/validate_agents.sh - Validate agent setup"
echo
echo "🎯 Usage Examples:"
echo "  @supervisor-orchestrator Build a React app"
echo "  @ai-scrum-master Set up sprint management"
echo "  @code-reviewer Review this code"
echo "  @test-automator Write unit tests for this feature"
echo
echo "✅ Ready to use Claude Code with 108 specialized sub-agents!"
EOF 