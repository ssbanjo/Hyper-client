
def _clear_payload(payload: dict):
    
    p = payload.copy()
    
    for key, value in payload.items():
        
        if value is None:
        
            del p[key]
            
        elif isinstance(value, dict):
            
            p[key] = _clear_payload(value)
            
    return p