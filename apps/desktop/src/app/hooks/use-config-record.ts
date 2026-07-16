import { useQuery } from '@tanstack/react-query'

import { getRayovinConfigRecord } from '@/rayovin'
import { queryClient, writeCache } from '@/lib/query-client'
import type { RayovinConfigRecord } from '@/types/rayovin'

// One shared cache for the whole profile config record (`GET /api/config`).
// Every settings surface (MCP, model, config) reads and writes through this key
// so a save in one shows in the others, and revisiting a tab paints the cache
// instead of blanking on a fresh fetch.
//
// Distinct from session/hooks/use-rayovin-config.ts, which is side-effecting —
// it pushes personality/cwd/voice/… into the session stores for live chat.
export const RAYOVIN_CONFIG_KEY = ['rayovin-config-record'] as const

// staleTime 0 → serve cache instantly, background-revalidate on every mount.
export const useRayovinConfigRecord = () =>
  useQuery({ queryKey: RAYOVIN_CONFIG_KEY, queryFn: getRayovinConfigRecord, staleTime: 0 })

export const setRayovinConfigCache = writeCache<RayovinConfigRecord>(RAYOVIN_CONFIG_KEY)

export const invalidateRayovinConfig = () => queryClient.invalidateQueries({ queryKey: RAYOVIN_CONFIG_KEY })
