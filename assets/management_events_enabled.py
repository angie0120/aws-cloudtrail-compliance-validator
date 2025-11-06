        management_events_enabled = False
        data_events_enabled = False
        
        event_selectors = trail.get('EventSelectors', [])
        for selector in event_selectors:
            if selector.get('ReadWriteType') in ['All', 'ReadOnly', 'WriteOnly']:
                management_events_enabled = selector.get('IncludeManagementEvents', False)
            
            data_resources = selector.get('DataResources', [])
            if data_resources:
                data_events_enabled = True
        
        validation_results['compliance_checks']['management_events'] = {
            'status': 'COMPLIANT' if management_events_enabled else 'NON_COMPLIANT',
            'value': management_events_enabled,
            'requirement': 'Management events must be logged for API call auditing'
        }