import json
from datetime import datetime
from pathlib import Path

def generate_sample_data():
    return {
        "summary": {
            "total_scanned_candidates": 4,
            "buy_review_count": 1,
            "manual_review_count": 3,
            "generated_at": datetime.utcnow().isoformat()
        },
        "results": [
            {
                "product": {
                    "source": "rogue",
                    "title": "Rogue Adjustable Bench 3.0",
                    "brand": "Rogue",
                    "sale_price": 595.00,
                    "availability": "in_stock",
                    "category_cluster": "strength_equipment"
                },
                "amazon_match": {
                    "asin": "B0ROGUE001",
                    "confidence": 0.92
                },
                "amazon_data": {
                    "competitive_price": 799.00,
                    "estimated_fees": 120.00
                },
                "net_profit": 84.00,
                "margin_percent": 10.5,
                "risk_flags": ["high_ticket", "shipping_cost"],
                "recommendation": "buy_review"
            },
            {
                "product": {
                    "source": "keiser",
                    "title": "Keiser M3i Indoor Cycle",
                    "brand": "Keiser",
                    "sale_price": 2295.00,
                    "availability": "in_stock",
                    "category_cluster": "cardio_equipment"
                },
                "amazon_match": {
                    "asin": "B0KEISER01",
                    "confidence": 0.88
                },
                "amazon_data": {
                    "competitive_price": 2699.00,
                    "estimated_fees": 350.00
                },
                "net_profit": 54.00,
                "margin_percent": 2.0,
                "risk_flags": ["high_ticket", "low_margin"],
                "recommendation": "manual_review"
            },
            {
                "product": {
                    "source": "woodway",
                    "title": "Woodway 4Front Treadmill",
                    "brand": "Woodway",
                    "sale_price": 6995.00,
                    "availability": "in_stock",
                    "category_cluster": "cardio_equipment"
                },
                "amazon_match": {
                    "asin": "B0WOODWAY1",
                    "confidence": 0.80
                },
                "amazon_data": {
                    "competitive_price": 7499.00,
                    "estimated_fees": 900.00
                },
                "net_profit": -396.00,
                "margin_percent": -5.3,
                "risk_flags": ["high_ticket", "oversized_item"],
                "recommendation": "manual_review"
            },
            {
                "product": {
                    "source": "lightforce",
                    "title": "LightForce FXi Therapy Laser",
                    "brand": "LightForce",
                    "sale_price": 12999.00,
                    "availability": "in_stock",
                    "category_cluster": "therapy_device"
                },
                "amazon_match": {
                    "asin": "B0LIGHTFORCE",
                    "confidence": 0.75
                },
                "amazon_data": {
                    "competitive_price": 13500.00,
                    "estimated_fees": 1500.00
                },
                "net_profit": -999.00,
                "margin_percent": -7.4,
                "risk_flags": ["medical_device", "manual_review_required"],
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
