#!/bin/bash

echo "🔧 Starting comprehensive agent organization fix..."

# Step 1: Consolidate testing agents into quality directory
echo "📊 Consolidating testing agents into quality directory..."
mv testing/api-tester.md quality/api-tester-testing.md 2>/dev/null
mv testing/performance-benchmarker.md quality/performance-benchmarker-testing.md 2>/dev/null
mv testing/test-results-analyzer.md quality/test-results-analyzer-testing.md 2>/dev/null
mv testing/tool-evaluator.md quality/tool-evaluator-testing.md 2>/dev/null
mv testing/workflow-optimizer.md quality/workflow-optimizer-testing.md 2>/dev/null

# Step 2: Consolidate project management agents into product directory
echo "📋 Consolidating project management agents into product directory..."
mv project-management/experiment-tracker.md product/experiment-tracker-pm.md 2>/dev/null
mv project-management/project-shipper.md product/project-shipper-pm.md 2>/dev/null
mv project-management/studio-producer.md product/studio-producer-pm.md 2>/dev/null

# Step 3: Consolidate engineering agents into development directory
echo "⚙️ Consolidating engineering agents into development directory..."
mv engineering/ai-engineer.md development/ai-engineer-eng.md 2>/dev/null
mv engineering/backend-architect.md development/backend-architect-eng.md 2>/dev/null
mv engineering/devops-automator.md development/devops-automator-eng.md 2>/dev/null
mv engineering/frontend-developer.md development/frontend-developer-eng.md 2>/dev/null
mv engineering/mobile-app-builder.md development/mobile-app-builder-eng.md 2>/dev/null
mv engineering/rapid-prototyper.md development/rapid-prototyper-eng.md 2>/dev/null
mv engineering/test-writer-fixer.md quality/test-writer-fixer-eng.md 2>/dev/null

# Step 4: Consolidate studio operations agents into operations directory
echo "🏢 Consolidating studio operations agents into operations directory..."
mv studio-operations/analytics-reporter.md operations/analytics-reporter-studio.md 2>/dev/null
mv studio-operations/finance-tracker.md operations/finance-tracker-studio.md 2>/dev/null
mv studio-operations/infrastructure-maintainer.md operations/infrastructure-maintainer-studio.md 2>/dev/null
mv studio-operations/legal-compliance-checker.md operations/legal-compliance-checker-studio.md 2>/dev/null
mv studio-operations/support-responder.md operations/support-responder-studio.md 2>/dev/null

# Step 5: Move rapid-prototyper from design to development (it's more of a development tool)
echo "🚀 Moving rapid-prototyper to development directory..."
mv design/rapid-prototyper.md development/rapid-prototyper-design.md 2>/dev/null

# Step 6: Move ai-engineer from data-ai to development (it's more of a development role)
echo "🤖 Moving ai-engineer to development directory..."
mv data-ai/ai-engineer.md development/ai-engineer-data.md 2>/dev/null

# Step 7: Remove empty directories
echo "🗑️ Removing empty directories..."
rmdir testing 2>/dev/null
rmdir project-management 2>/dev/null
rmdir engineering 2>/dev/null
rmdir studio-operations 2>/dev/null

# Step 8: Create a summary of duplicates for manual review
echo "📝 Creating duplicate summary..."
cat > duplicate_summary.md << 'EOF'
# Duplicate Agent Files Summary

## Testing Agents (Consolidated into quality/)
- api-tester.md → quality/api-tester-testing.md
- performance-benchmarker.md → quality/performance-benchmarker-testing.md  
- test-results-analyzer.md → quality/test-results-analyzer-testing.md
- tool-evaluator.md → quality/tool-evaluator-testing.md
- workflow-optimizer.md → quality/workflow-optimizer-testing.md

## Project Management Agents (Consolidated into product/)
- experiment-tracker.md → product/experiment-tracker-pm.md
- project-shipper.md → product/project-shipper-pm.md
- studio-producer.md → product/studio-producer-pm.md

## Engineering Agents (Consolidated into development/)
- ai-engineer.md → development/ai-engineer-eng.md
- backend-architect.md → development/backend-architect-eng.md
- devops-automator.md → development/devops-automator-eng.md
- frontend-developer.md → development/frontend-developer-eng.md
- mobile-app-builder.md → development/mobile-app-builder-eng.md
- rapid-prototyper.md → development/rapid-prototyper-eng.md
- test-writer-fixer.md → quality/test-writer-fixer-eng.md

## Studio Operations Agents (Consolidated into operations/)
- analytics-reporter.md → operations/analytics-reporter-studio.md
- finance-tracker.md → operations/finance-tracker-studio.md
- infrastructure-maintainer.md → operations/infrastructure-maintainer-studio.md
- legal-compliance-checker.md → operations/legal-compliance-checker-studio.md
- support-responder.md → operations/support-responder-studio.md

## Other Moves
- design/rapid-prototyper.md → development/rapid-prototyper-design.md
- data-ai/ai-engineer.md → development/ai-engineer-data.md

## Next Steps
1. Review duplicate files and merge content if needed
2. Update README.md to reflect new organization
3. Update any references to moved files
EOF

echo "✅ Organization fix completed!"
echo "📋 Check duplicate_summary.md for details on moved files" 