import base64
class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = [base64.b64encode(s.encode()).decode() + ","  for s in strs]
        joined = "".join(parts)
        return joined

    def decode(self, s: str) -> List[str]:
        back = [base64.b64decode(p).decode() for p in s.split(",")[:-1] ]
        return back