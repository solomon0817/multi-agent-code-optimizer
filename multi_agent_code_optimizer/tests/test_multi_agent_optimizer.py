import pytest
from src.multi_agent_optimizer import MultiAgentCodeOptimizer

def test_multi_agent_optimizer():
    code = "int variable = 0;"
    optimizer = MultiAgentCodeOptimizer(code)
    optimized_code, analysis_result, compliance_result = optimizer.analyze_and_optimize()

    # Check if the optimization worked and compliance issues
    assert optimized_code == "for i in range(1, n+1)"  # Example optimized result
    assert 'Avoid redundant variable initializations.' in analysis_result['suggestions']
    assert len(compliance_result['compliance_issues']) == 0  # Assuming the code passed compliance checks
