import json
import os
import sys
import re

def check_guardrails():
    js_path = os.path.join(os.path.dirname(__file__), "../data/validation_data.js")
    if not os.path.exists(js_path):
        print(f"Error: Validation data file not found at {js_path}", file=sys.stderr)
        sys.exit(1)
        
    with open(js_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Strip window.validationData = 
    json_str = re.sub(r"^window\.validationData\s*=\s*", "", content).strip()
    if json_str.endswith(";"):
        json_str = json_str[:-1]
        
    try:
        data = json.loads(json_str)
    except Exception as e:
        print(f"Error parsing JSON from {js_path}: {e}", file=sys.stderr)
        sys.exit(1)
        
    errors = []
    
    def check_node(node, path_name):
        # Check accuracy dict
        acc = node.get("accuracy", {})
        for k, v in acc.items():
            if isinstance(v, (int, float)):
                if v < 100.0:
                    errors.append(f"Mismatch at '{path_name}': Feature '{k}' accuracy is {v}% (expected 100.0%)")
            
        # Check details accuracies
        details = node.get("details", {})
        for k, v in details.items():
            if isinstance(v, dict) and "accuracy" in v:
                v_acc = v["accuracy"]
                if isinstance(v_acc, (int, float)) and v_acc < 100.0:
                    errors.append(f"Mismatch at '{path_name}': Detail feature '{k}' accuracy is {v_acc}% (expected 100.0%)")
                    
        # Recurse children
        for child in node.get("children", []):
            child_name = child.get("name", "Unknown")
            check_node(child, f"{path_name} -> {child_name}")

    check_node(data, data.get("name", "University"))
    
    if errors:
        print(f"--- Guardrail Checks FAILED ({len(errors)} errors) ---", file=sys.stderr)
        for err in errors[:20]:
            print(err, file=sys.stderr)
        if len(errors) > 20:
            print(f"... and {len(errors) - 20} more errors.", file=sys.stderr)
        sys.exit(1)
        
    print("--- Guardrail Checks PASSED (All metrics are exactly 100.0%) ---")
    sys.exit(0)

if __name__ == "__main__":
    check_guardrails()
