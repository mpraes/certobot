"""
Redis configuration and connection management.
Handles Redis connection for caching and session management.
"""

import json
from typing import Any, Optional

import redis.asyncio as redis
from redis.asyncio import Redis

from backend.core.settings import settings

# Global Redis connection
_redis_client: Optional[Redis] = None


async def get_redis() -> Redis:
    """Get Redis client instance."""
    global _redis_client
    
    if _redis_client is None:
        _redis_client = redis.from_url(
            settings.redis_url,
            encoding="utf-8",
            decode_responses=True,
        )
    
    return _redis_client


async def close_redis():
    """Close Redis connection."""
    global _redis_client
    
    if _redis_client:
        await _redis_client.close()
        _redis_client = None


class RedisCache:
    """Redis cache utility class."""
    
    def __init__(self):
        self._client: Optional[Redis] = None
    
    async def _get_client(self) -> Redis:
        """Get Redis client."""
        if self._client is None:
            self._client = await get_redis()
        return self._client
    
    async def set(
        self,
        key: str,
        value: Any,
        expire: Optional[int] = None
    ) -> bool:
        """Set a value in Redis with optional expiration."""
        client = await self._get_client()
        
        # Serialize value to JSON if it's not a string
        if not isinstance(value, str):
            value = json.dumps(value, default=str)
        
        return await client.set(key, value, ex=expire)
    
    async def get(self, key: str) -> Optional[str]:
        """Get a value from Redis."""
        client = await self._get_client()
        return await client.get(key)
    
    async def get_json(self, key: str) -> Optional[Any]:
        """Get a JSON value from Redis and deserialize it."""
        value = await self.get(key)
        if value is None:
            return None
        
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value
    
    async def delete(self, key: str) -> bool:
        """Delete a key from Redis."""
        client = await self._get_client()
        return bool(await client.delete(key))
    
    async def exists(self, key: str) -> bool:
        """Check if a key exists in Redis."""
        client = await self._get_client()
        return bool(await client.exists(key))
    
    async def expire(self, key: str, seconds: int) -> bool:
        """Set expiration time for a key."""
        client = await self._get_client()
        return bool(await client.expire(key, seconds))


# Global cache instance
cache = RedisCache()