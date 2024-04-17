from .Dummy import dummy_stateful_metrics
from .Investment import investment_stateful_metric_sets

stateful_metrics = []
stateful_metrics.extend(dummy_stateful_metrics)
stateful_metrics.extend(investment_stateful_metric_sets)
