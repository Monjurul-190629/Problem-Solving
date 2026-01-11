t = int(input())

for i in range(t):
    st = input().strip()
    if st.startswith("http://"):
        redirected_url = "https://" + st[7:]
    else:
        redirected_url = st
    print(f'Case {i + 1}:', redirected_url)