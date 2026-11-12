def minimumTeam(skills, candidates):
    skill_to_idx = {s: i for i, s in enumerate(skills)}
    req_mask = (1 << len(skills)) - 1
    cand_masks = []
    for c in candidates:
        mask = 0
        for s in c:
            if s in skill_to_idx:
                mask |= (1 << skill_to_idx[s])
        cand_masks.append(mask)
    
    best_team = []
    def dfs(mask, index, current_team):
        nonlocal best_team
        if mask == req_mask:
            if not best_team or len(current_team) < len(best_team):
                best_team = list(current_team)
            return
        if index == len(cand_masks) or (best_team and len(current_team) >= len(best_team)):
            return
        dfs(mask, index + 1, current_team)
        dfs(mask | cand_masks[index], index + 1, current_team + [index])
        
    dfs(0, 0, [])
    return best_team

if __name__ == "__main__":
    skills = ["Python", "SQL", "Machine Learning", "DataStructures"]
    cands = [["Python", "SQL"], ["SQL", "Machine Learning"], ["Machine Learning", "DataStructures"], ["DataStructures"]]
    print("Example 1:", minimumTeam(skills, cands))
