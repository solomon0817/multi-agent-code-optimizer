import agent_code_analyzer
import agent_performance_optimizer
import agent_code_compliance

class MultiAgentCodeOptimizer:
    def __init__(self, code):
        self.code = code

    def analyze_and_optimize(self):
        # Code Analysis Agent
        analysis_result = agent_code_analyzer.analyze_code(self.code)

        # Performance Optimization Agent
        optimized_code = agent_performance_optimizer.optimize_performance(self.code)

        # Code Compliance Agent
        compliance_result = agent_code_compliance.check_compliance(optimized_code)

        return optimized_code, analysis_result, compliance_result
