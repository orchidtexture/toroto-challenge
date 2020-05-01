import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import Drawer from "@material-ui/core/Drawer";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import AccountBoxIcon from "@material-ui/icons/AccountBox";
import NotesIcon from "@material-ui/icons/Notes";
import ExitToAppIcon from "@material-ui/icons/ExitToApp";
import Typography from "@material-ui/core/Typography";
import IconButton from "@material-ui/core/IconButton";
import Hidden from "@material-ui/core/Hidden";
import Divider from "@material-ui/core/Divider";
import MenuIcon from "@material-ui/icons/Menu";
import CloseIcon from "@material-ui/icons/Close";

const drawerWidth = 240;

const styles = (theme) => ({
  root: {
    display: "flex",
  },
  appBar: {
    position: "fixed",
    zIndex: theme.zIndex.drawer + 1,
  },
  navIconHide: {
    [theme.breakpoints.up("md")]: {
      display: "none",
    },
  },
  toolbar: theme.mixins.toolbar,
  drawer: {
    width: drawerWidth,
    flexShrink: 0,
  },
  drawerPaper: {
    width: drawerWidth,
    [theme.breakpoints.up("sm")]: {
      position: "absolute",
    },
  },
  content: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.default,
  },
});

class ResponsiveDrawer extends React.Component {
  state = {
    mobileOpen: false,
  };

  handleDrawerToggle = () => {
    this.setState((state) => ({ mobileOpen: !state.mobileOpen }));
  };

  render() {
    const { classes } = this.props;

    const drawer = (
      <div>
        <div className={classes.toolbar}>
          <IconButton
            button
            color="inherit"
            aria-label="Close drawer"
            key="Close"
            onClick={this.handleDrawerToggle}
          >
            <CloseIcon />
          </IconButton>
        </div>
        <Divider />
        <center>
          <p>{this.props.drawerData.firstName}</p>
        </center>
        <Divider />
        <List>
          <ListItem
            button
            key="Subscribers"
            onClick={this.props.drawerData.loadListPage}
          >
            <ListItemIcon>
              {" "}
              <NotesIcon />{" "}
            </ListItemIcon>
            <ListItemText primary="Subscribers" />
          </ListItem>

          <ListItem
            button
            key="Account"
            onClick={this.props.drawerData.loadAccountPage}
          >
            <ListItemIcon>
              {" "}
              <AccountBoxIcon />{" "}
            </ListItemIcon>
            <ListItemText primary="Account" />
          </ListItem>

          <ListItem
            button
            key="Logout"
            onClick={this.props.drawerData.logoutHandler}
          >
            <ListItemIcon>
              {" "}
              <ExitToAppIcon />{" "}
            </ListItemIcon>
            <ListItemText primary="Logout" />
          </ListItem>
        </List>
      </div>
    );

    return (
      <div className={classes.root}>
        <AppBar className={classes.appBar}>
          <Toolbar>
            <IconButton
              color="inherit"
              aria-label="Open drawer"
              onClick={this.handleDrawerToggle}
              className={classes.navIconHide}
            >
              <MenuIcon />
            </IconButton>
            <Typography variant="h6" noWrap>
              Subscribers
            </Typography>
          </Toolbar>
        </AppBar>
        <Hidden mdUp>
          <Drawer
            className={classes.drawer}
            variant="temporary"
            // anchor={theme.direction === "rtl" ? "right" : "left"}
            open={this.state.mobileOpen}
            onClose={this.handleDrawerToggle}
            classes={{
              paper: classes.drawerPaper,
            }}
            ModalProps={{
              keepMounted: true, // Better open performance on mobile.
            }}
          >
            {drawer}
          </Drawer>
        </Hidden>
        <Hidden smDown implementation="js">
          <Drawer
            className={classes.drawer}
            variant="permanent"
            open
            classes={{
              paper: classes.drawerPaper,
            }}
          >
            {drawer}
          </Drawer>
        </Hidden>
        <main className={classes.content}>
          <div className={classes.toolbar} />
        </main>
      </div>
    );
  }
}

ResponsiveDrawer.propTypes = {
  classes: PropTypes.object.isRequired,
  theme: PropTypes.object.isRequired,
};

export default withStyles(styles, { withTheme: true })(ResponsiveDrawer);
