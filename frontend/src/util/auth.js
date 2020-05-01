export const authMiddleWare = (history) => {
  const authToken = localStorage.getItem("token");
  if (authToken === null) {
    history.push("/login");
  }
};
