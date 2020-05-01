import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import signup from "./pages/signup";
import login from "./pages/login";
import home from "./pages/home";
import { ThemeProvider as MuiThemeProvider } from "@material-ui/core/styles";
import createMuiTheme from "@material-ui/core/styles/createMuiTheme";

const theme = createMuiTheme({
  palette: {
    primary: {
      main: "#1930db",
      contrastText: "#fff",
    },
  },
});

function App() {
  return (
    <MuiThemeProvider theme={theme}>
      <div>
        <Router>
          <div>
            <Switch>
              <Route exact path="/signup" component={signup} />
              <Route exact path="/login" component={login} />
              <Route exact path="/" component={home} />
            </Switch>
          </div>
        </Router>
      </div>
    </MuiThemeProvider>
  );
}
export default App;
