#!/bin/bash

echo "🧹 Cleaning up untracked files and organizing documentation..."

# Remove backup files created during optimization
echo "🗑️ Removing backup files..."
find . -name "*.bak" -type f -delete
echo "✅ Removed $(find . -name "*.bak" -type f | wc -l) backup files"

# Create documentation directory
mkdir -p docs

# Move documentation files to docs directory
echo "📁 Moving documentation files to docs/ directory..."
mv CLAUDE_CODE_READY.md docs/ 2>/dev/null
mv SETUP_GUIDE.md docs/ 2>/dev/null
mv FINAL_OPTIMIZATION_SUMMARY.md docs/ 2>/dev/null
mv SCRUM_MASTER_ADDED.md docs/ 2>/dev/null
mv ORGANIZATION_COMPLETE.md docs/ 2>/dev/null
mv FINAL_SUMMARY.md docs/ 2>/dev/null
mv MASTER_AGENT_CATALOG.md docs/ 2>/dev/null
mv COMPREHENSIVE_ANALYSIS.md docs/ 2>/dev/null
mv CLAUDE.md docs/ 2>/dev/null
mv duplicate_summary.md docs/ 2>/dev/null
mv final_organization_report.md docs/ 2>/dev/null

# Move agent files that should be in .claude/agents
echo "📋 Moving agent files to proper locations..."
if [ -f "ai-scrum-master.md" ]; then
    mv ai-scrum-master.md .claude/agents/product/ 2>/dev/null
fi

if [ -f "supervisor-orchestrator.md" ]; then
    mv supervisor-orchestrator.md .claude/agents/orchestration/ 2>/dev/null
fi

# Create a clean README for the project
echo "📝 Creating clean project README..."
cat > README.md << 'EOF'
# 🚀 Claude Code Sub-Agents Collection

A comprehensive collection of **110 specialized AI sub-agents** optimized for Claude Code with parallel execution capabilities, enhanced communication protocols, and comprehensive quality assurance.

## 🎯 Quick Start

### **Setup**
```bash
# Run the setup script
./setup_claude_agents.sh

# Optimize all agents
./optimize_agents.sh

# Validate setup
./.claude/validate_agents.sh
```

### **Usage**
```bash
# Start with orchestrator for complex projects
@supervisor-orchestrator Build a React e-commerce app

# Set up sprint management
@ai-scrum-master Set up automated sprint management

# Review code with parallel testing
@code-reviewer Review this codebase
```

## 📊 Agent Distribution

| Category | Count | Status |
|----------|-------|--------|
| 🎯 Orchestration & Management | 6 | ✅ Enhanced |
| 🏗️ Development & Architecture | 24 | ✅ Enhanced |
| 🎨 Design & UX | 7 | ✅ Enhanced |
| 🔧 Quality Assurance & Testing | 15 | ✅ Enhanced |
| 🔒 Security & Compliance | 4 | ✅ Enhanced |
| 📊 Data & AI | 4 | ✅ Enhanced |
| 🚀 DevOps & Infrastructure | 13 | ✅ Enhanced |
| 📝 Documentation & Communication | 6 | ✅ Enhanced |
| 🎯 Product & Business | 9 | ✅ Enhanced |
| 📈 Marketing & Growth | 7 | ✅ Enhanced |
| 🏢 Operations | 5 | ✅ Enhanced |
| 🎭 Specialized & Utility | 9 | ✅ Enhanced |
| **Total** | **110** | **100% Optimized** |

## 🚀 Key Features

- ✅ **Parallel Execution**: All agents can work simultaneously
- ✅ **Enhanced Communication**: Standardized protocols across all agents
- ✅ **Quality Gates**: Built-in validation and review processes
- ✅ **Intelligent Coordination**: Optimal agent selection and delegation
- ✅ **Comprehensive Documentation**: Complete setup and usage guides

## 📁 Project Structure

```
agents/
├── .claude/                    # Claude Code configuration
│   ├── agents/                # All 110 optimized agents
│   ├── config.json           # Claude Code configuration
│   └── optimization/         # Optimization settings
├── docs/                     # Documentation
├── setup_claude_agents.sh    # Setup script
├── optimize_agents.sh        # Optimization script
└── README.md                # This file
```

## 🎯 Usage Examples

### **Development Projects**
```
@supervisor-orchestrator Build a React e-commerce app with payment integration
```

### **Business Projects**
```
@supervisor-orchestrator Launch a meditation app with marketing strategy
```

### **Sprint Management**
```
@ai-scrum-master Set up automated sprint management for the development team
```

### **Quality Assurance**
```
@code-reviewer Review this codebase with parallel testing
```

## 📋 Available Commands

- `./.claude/discover_agents.sh` - Discover all agents
- `./.claude/validate_agents.sh` - Validate agent setup
- `@supervisor-orchestrator` - Master coordinator for complex projects
- `@ai-scrum-master` - Automated sprint management
- `@code-reviewer` - Code review and quality assurance
- `@test-automator` - Automated testing

## 🎉 Success Metrics

- **Parallel Efficiency**: >80% parallel task completion
- **Task Completion**: >90% successful task completion
- **Quality Score**: >95% quality standards maintained
- **Coordination Effectiveness**: >85% effective agent coordination

---

**🎉 Ready to use with 110 optimized agents featuring parallel execution, enhanced communication, and comprehensive quality assurance! 🚀**
EOF

# Create a .gitignore file
echo "📝 Creating .gitignore file..."
cat > .gitignore << 'EOF'
# Backup files
*.bak
*.backup

# Temporary files
*.tmp
*.temp

# Log files
*.log

# OS files
.DS_Store
Thumbs.db

# IDE files
.vscode/
.idea/
*.swp
*.swo

# Node modules (if any)
node_modules/

# Environment files
.env
.env.local
.env.production

# Build outputs
dist/
build/
EOF

echo "✅ Cleanup complete!"
echo
echo "📊 Cleanup Summary:"
echo "  - Removed $(find . -name "*.bak" -type f | wc -l) backup files"
echo "  - Moved documentation to docs/ directory"
echo "  - Organized agent files in proper locations"
echo "  - Created clean project README"
echo "  - Added .gitignore file"
echo
echo "📁 New structure:"
echo "  - docs/ - All documentation files"
echo "  - .claude/agents/ - All 110 optimized agents"
echo "  - README.md - Clean project overview"
echo
echo "🎯 Ready for production use!" 