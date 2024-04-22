def validate_cpf(cpf):

    valid_chars = "-.0123456789"
    if len([unv_c for unv_c in cpf if unv_c not in valid_chars]) > 0:
        return False
    
    cpf_ = cpf.split('-')
    if len(cpf_) != 2:
        return False
    
    if len(cpf_[1]) != 2 or "." in cpf_[1]:
        return False
    
    start_cpf = cpf_[0].split(".")
    if len(start_cpf) != 3:
        return False
    
    for part in start_cpf:
        if len(part) != 3:
            return False
    
    return True

