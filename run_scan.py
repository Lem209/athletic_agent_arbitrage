import json
from datetime import datetime
from pathlib import Path

def generate_sample_data():
    return {
        "summary": {
            "total_scanned_candidates": 10,
            "buy_review_count": 2,
            "manual_review_count": 3,
            "generated_at": datetime.utcnow().isoformat()
        },
        "results": [
            {
                "product": {
                    "source": "academy",
                    "title": "Adjustable Kettlebell 40 lb",
                    "brand": "ExampleBrand",
                    "sale_price": 39.99,
                    "availability": "in_stock",
                    "category_cluster": "exercise_equipment"
                },
                "amazon_match": {
                    "asin": "B0EXAMPLE1",
                    "confidence": 0.96
                },
                "amazon_data": {
                    "competitive_price": 74.99,
                    "estimated_fees": 18.44
                },
                "net_profit": 12.50,
                "margin_percent": 18.2,
                "risk_flags": [],
                "recommendation": "buy_review"
            },
            {
                "product": {
                    "source": "dicks",
                    "title": "Foam Roller Recovery Tool",
                    "brand": "RecoveryPro",
                    "sale_price": 14.99,
                    "availability": "in_stock",
                    "category_cluster": "health_wellness"
                },
                "amazon_match": {
                    "asin": "B0EXAMPLE2",
                    "confidence": 0.91
                },
                "amazon_data": {
                    "competitive_price": 29.99,
                    "estimated_fees": 8.00
                },
                "net_profit": 5.00,
                "margin_percent": 16.7,
                "risk_flags": ["low_margin"],
                "recommendation": "manual_review"
            }
        ]
    }

def main():
    data = generate_sample_data()
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    with open(output_dir / "latest_summary.json", "w") as f:
        json.dump(data["summary"], f, indent=2)

    with open(output_dir / "latest_opportunities.json", "w") as f:
        json.dump(data["results"], f, indent=2)

    print("Scan complete! Results saved in the 'outputs' folder.")

if __name__ == "__main__":
    main()
