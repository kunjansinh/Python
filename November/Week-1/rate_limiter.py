from collections import deque
import time


class SlidingWindowRateLimiter:
    """Sliding window rate limiter using monotonic timestamps."""

    def __init__(self, max_requests: int, window_seconds: float) -> None:
        if max_requests <= 0 or window_seconds <= 0:
            raise ValueError("max_requests and window_seconds must be positive.")
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._requests: dict[str, deque[float]] = {}

    def allow_request(self, client_id: str) -> bool:
        """Return True if the client is within the rate limit, False otherwise."""
        now = time.monotonic()
        window_start = now - self.window_seconds

        timestamps = self._requests.setdefault(client_id, deque())

        # Evict timestamps outside the active time window
        while timestamps and timestamps[0] <= window_start:
            timestamps.popleft()

        if len(timestamps) < self.max_requests:
            timestamps.append(now)
            return True

        return False


if __name__ == "__main__":
    limiter = SlidingWindowRateLimiter(max_requests=3, window_seconds=2.0)

    for attempt in range(1, 6):
        allowed = limiter.allow_request("user_101")
        print(f"Request {attempt}: {'ALLOWED' if allowed else 'BLOCKED'}")
        time.sleep(0.4)