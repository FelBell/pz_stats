-- PZStats_Events.lua
-- Skeleton for tracking player deaths and zombie kills

local function OnZombieDead(zombie)
    local killer = zombie:getAttacker()
    if killer and killer:getObjectName() == "IsoPlayer" then
        local username = "Unknown"
        if killer.getUsername then
            username = killer:getUsername()
        end
        -- Log format for log-forwarder: [PZSTATS] JSON
        print("[PZSTATS] " .. '{"event": "zombie_kill", "username": "' .. username .. '"}')
    end
end

local function OnPlayerDeath(player)
    local username = "Unknown"
    if player.getUsername then
        username = player:getUsername()
    end
    -- Log format for log-forwarder: [PZSTATS] JSON
    print("[PZSTATS] " .. '{"event": "player_death", "username": "' .. username .. '"}')
end

-- Register events
Events.OnZombieDead.Add(OnZombieDead)
Events.OnPlayerDeath.Add(OnPlayerDeath)

print("PZStats: Mod loaded successfully.")
