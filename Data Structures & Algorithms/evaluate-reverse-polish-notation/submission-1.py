class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st = []

        for token in tokens:
            if token == "+":
                a = st.pop()
                b = st.pop()
                st.append(b + a)

            elif token == "-":
                a = st.pop()
                b = st.pop()
                st.append(b - a)

            elif token == "*":
                a = st.pop()
                b = st.pop()
                st.append(b * a)

            elif token == "/":
                a = st.pop()
                b = st.pop()
                st.append(int(b / a))  # truncate toward 0

            else:
                st.append(int(token))

        return st[-1]
