def outer_function():
    def inner_function():
        return "Hello from the inner function!"
    
    result = inner_function() 
    return result