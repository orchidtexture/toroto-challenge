import React, { Component } from "react";
import axios from "axios";

import Account from "../components/account";
import Subscribers from "../components/subscriber";
import ResponsiveDrawer from "../components/sidebar";

import CssBaseline from "@material-ui/core/CssBaseline";
import withStyles from "@material-ui/core/styles/withStyles";
import CircularProgress from "@material-ui/core/CircularProgress";

import { authMiddleWare } from "../util/auth";

const drawerWidth = 240;

const styles = (theme) => ({
  root: {
    display: "flex",
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(3),
  },
  uiProgess: {
    position: "fixed",
    zIndex: "1000",
    height: "31px",
    width: "31px",
    left: "50%",
    top: "35%",
  },
});

class home extends Component {
  state = {
    render: false,
  };

  loadAccountPage = (event) => {
    this.setState({ render: true });
  };

  loadSubscriberPage = (event) => {
    this.setState({ render: false });
  };

  logoutHandler = (event) => {
    localStorage.removeItem("token");
    this.props.history.push("/login");
  };

  constructor(props) {
    super(props);

    this.state = {
      firstName: "",
      lastName: "",
      uiLoading: true,
      imageLoading: false,
    };
  }

  componentWillMount = () => {
    authMiddleWare(this.props.history);
    const token = localStorage.getItem("token");
    axios.defaults.headers.common = { Authorization: `${token}` };
    axios
      .get("/api/v1/users/")
      .then((response) => {
        console.log(response.data.first_name);
        this.setState({
          firstName: response.data.first_name,
          lastName: response.data.last_name,
          email: response.data.email,
          uiLoading: false,
        });
      })
      .catch((error) => {
        if (error.response.status === 403) {
          this.props.history.push("/login");
        }
        console.log(error);
        this.setState({ errorMsg: "Error in retrieving the data" });
      });
  };

  render() {
    const { classes } = this.props;
    if (this.state.uiLoading === true) {
      return (
        <div className={classes.root}>
          {this.state.uiLoading && (
            <CircularProgress size={150} className={classes.uiProgess} />
          )}
        </div>
      );
    } else {
      const drawerData = {
        firstName: this.state.firstName,
        lastName: this.state.lastName,
        loadSubscriberPage: this.loadSubscriberPage,
        loadAccountPage: this.loadAccountPage,
        logoutHandler: this.logoutHandler,
      };
      return (
        <div className={classes.root}>
          <CssBaseline />
          <ResponsiveDrawer drawerData={drawerData} />

          <div>{this.state.render ? <Account /> : <Subscribers />}</div>
        </div>
      );
    }
  }
}

export default withStyles(styles)(home);
