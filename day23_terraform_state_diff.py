
def state_diff(old_state, new_state):
    """
    Compares two Terraform state files and returns the differences.

    Args:
        old_state (dict): The old Terraform state.
        new_state (dict): The new Terraform state.
    Returns:
        dict: A dictionary containing the differences between the two states.
    """
    diff = {
        "added": {},
        "removed": {},
        "changed": {}
    }

    for key in new_state:
        if key not in old_state:
            diff["added"][key] = new_state[key]
            
    for key in old_state:
        if key not in new_state:
            diff["removed"][key] = old_state[key]
            
    for key in old_state:
        if key in new_state and old_state[key] != new_state[key]:
            diff["changed"][key] = {
                "old": old_state[key],
                "new": new_state[key]
            }
            
    return diff


if __name__ == "__main__":
    old = {"instance_type": "t3.micro", "region": "us-east-1", "count": 2}
    new = {"instance_type": "t3.medium", "region": "us-east-1", "count": 3, "tags": {"env": "prod"}}
    print(state_diff(old, new))