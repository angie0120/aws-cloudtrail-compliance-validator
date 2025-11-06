    def _initialize_clients(self):
        """Initialize AWS clients with optional profile support."""
        try:
            if self.profile_name:
                logger.info(f"Using AWS profile: {self.profile_name}")
                self.session = boto3.Session(profile_name=self.profile_name)
            else:
                logger.info("Using default AWS credentials")
                self.session = boto3.Session()
            
            self.cloudtrail_client = self.session.client('cloudtrail', region_name=self.region_name)
            self.s3_client = self.session.client('s3', region_name=self.region_name)
            self.sts_client = self.session.client('sts', region_name=self.region_name)
            
            # Get account ID
            response = self.sts_client.get_caller_identity()
            self.account_id = response['Account']
            logger.info(f"Connected to AWS Account: {self.account_id}")