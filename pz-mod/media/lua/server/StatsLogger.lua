if isClient() then return end -- Server side only

local StatsLogger = {}

local function log_stat(player_name, event_type, data_str)
    -- Simple manual JSON formatting
    local json = string.format('{"player": "%s", "event": "%s", "data": "%s"}',
        player_name, event_type, data_str)
    print("[PZ_STATS] " .. json)
end

-- Example Hook: Player Death
Events.OnPlayerDeath.Add(function(player)
    log_stat(player:getUsername(), "death", "Died")
end)

-- Example Hook: Every 10 minutes log uptime (Just to show it works)
local function log_uptime()
    print("[PZ_STATS] {\"player\": \"System\", \"event\": \"heartbeat\", \"data\": \"Server Running\"}")
end

-- Note: In a real server, ensure Events.EveryTenMinutes is available or use a Tick counter.
if Events.EveryTenMinutes then
    Events.EveryTenMinutes.Add(log_uptime)
end

print("PZ Stats Mod Loaded")
