    def save_json_report(self, report: Dict[str, Any], filename: str = None):
        """Save compliance report as JSON file."""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"cloudtrail_compliance_report_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        logger.info(f"JSON report saved: {filename}")
        return filename