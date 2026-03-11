
def dependency_resolver(dependencies):
    
    d = {k: set(v) for k, v in dependencies.items()}
    resolve = []
    
    while d:
        
        no_deps = set(k for k, v in d.items() if not v)
        if not no_deps:
            raise ValueError("Circular Dependency Detected!")
        resolve.append(no_deps)
        
        # Remove resolved dependencies
        for dep in no_deps:
            del d[dep]
        for k in d:
            d[k] = {dep for dep in d[k] if dep not in no_deps}
        
    return [item for level in resolve for item in level]
        
        



if __name__ == "__main__":
    deps = {"app": ["flask", "redis"], "flask": ["jinja2"], "redis": [], "jinja2": []}
    print(dependency_resolver(deps)) 
    
    deps = {"a": ["b"], "b": ["c"], "c": []}
    print(dependency_resolver(deps))
    
    deps = {"a": ["b"], "b": ["a"]}
    print(dependency_resolver(deps))