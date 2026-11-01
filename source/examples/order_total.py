"""NiFi ExecuteStreamCommand example: read one JSON object and write JSON."""
import json
import sys
from decimal import Decimal

order = json.load(sys.stdin)
order["total_amount"] = float(
    Decimal(str(order["quantity"])) * Decimal(str(order["unit_price"]))
)
json.dump(order, sys.stdout, ensure_ascii=False)
