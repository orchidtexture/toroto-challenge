import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import Dialog from "@material-ui/core/Dialog";
import AddCircleIcon from "@material-ui/icons/AddCircle";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import IconButton from "@material-ui/core/IconButton";
import CloseIcon from "@material-ui/icons/Close";
import Slide from "@material-ui/core/Slide";
import TextField from "@material-ui/core/TextField";
import Grid from "@material-ui/core/Grid";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CircularProgress from "@material-ui/core/CircularProgress";
import CardContent from "@material-ui/core/CardContent";
import MuiDialogTitle from "@material-ui/core/DialogTitle";
import MuiDialogContent from "@material-ui/core/DialogContent";

import axios from "axios";
import { authMiddleWare } from "../util/auth";

import withStyles from "@material-ui/core/styles/withStyles";
import Typography from "@material-ui/core/Typography";

const styles = (theme) => ({
  content: {
    flexGrow: 1,
    padding: theme.spacing(3),
  },
  toolbar: theme.mixins.toolbar,
  name: {
    marginLeft: theme.spacing(2),
    flex: 1,
  },
  submitButton: {
    display: "block",
    color: "white",
    textAlign: "center",
    position: "absolute",
    top: 14,
    right: 10,
  },
  floatingButton: {
    position: "fixed",
    bottom: 0,
    right: 0,
  },
  form: {
    width: "98%",
    marginLeft: 13,
    marginTop: theme.spacing(3),
  },
  toolbar: theme.mixins.toolbar,
  root: {
    minWidth: 470,
  },
  bullet: {
    display: "inline-block",
    margin: "0 2px",
    transform: "scale(0.8)",
  },
  pos: {
    marginBottom: 12,
  },
  uiProgess: {
    position: "fixed",
    zIndex: "1000",
    height: "31px",
    width: "31px",
    left: "50%",
    top: "35%",
  },
  dialogeStyle: {
    maxWidth: "50%",
  },
  viewRoot: {
    margin: 0,
    padding: theme.spacing(2),
  },
  closeButton: {
    position: "absolute",
    right: theme.spacing(1),
    top: theme.spacing(1),
    color: theme.palette.grey[500],
  },
});

const Transition = React.forwardRef(function Transition(props, ref) {
  return <Slide direction="up" ref={ref} {...props} />;
});

class subscriber extends Component {
  constructor(props) {
    super(props);

    this.state = {
      subscribers: "",
      firstName: "",
      lastName: "",
      co2PerYear: "",
      subscriberId: "",
      subscription: "",
      monthlyFee: "",
      co2PerMonth: "",
      hasSubscription: "",
      errors: [],
      open: false,
      uiLoading: true,
      buttonType: "",
      viewOpen: false,
    };

    this.deleteTodoHandler = this.deleteTodoHandler.bind(this);
    this.handleEditClickOpen = this.handleEditClickOpen.bind(this);
    this.handleViewOpen = this.handleViewOpen.bind(this);
  }

  handleChange = (event) => {
    this.setState({
      [event.target.name]: event.target.value,
    });
  };

  componentWillMount = () => {
    authMiddleWare(this.props.history);
    const token = localStorage.getItem("token");
    axios.defaults.headers.common = { Authorization: `${token}` };
    axios
      .get("/api/v1/subscribers/")
      .then((response) => {
        this.setState({
          subscribers: response.data,
          uiLoading: false,
        });
      })
      .catch((err) => {
        console.log(err);
      });
  };

  deleteTodoHandler(data) {
    authMiddleWare(this.props.history);
    const token = localStorage.getItem("token");
    axios.defaults.headers.common = { Authorization: `${token}` };
    let subscriberId = data.subscriber.id;
    axios
      .delete(`api/v1/subscribers/${subscriberId}`)
      .then(() => {
        window.location.reload();
      })
      .catch((err) => {
        console.log(err);
      });
  }

  createSubscribeHandler(data) {
    authMiddleWare(this.props.history);
    const token = localStorage.getItem("token");
    axios.defaults.headers.common = { Authorization: `${token}` };
    const subscriberData = {
      subscriber_id: data.subscriber.id,
    };
    let options = {
      url: "api/v1/subscriptions/",
      method: "post",
      data: subscriberData,
    };
    axios(options)
      .then(() => {
        window.location.reload();
      })
      .catch((err) => {
        console.log(err);
      });
  }

  handleEditClickOpen(data) {
    console.log(data.subscriber.has_subscription);
    if (data.subscriber.subscription != null) {
      this.setState({
        firstName: data.subscriber.first_name,
        lastName: data.subscriber.last_name,
        email: data.subscriber.email,
        co2PerYear: data.subscriber.co2_tons_per_year,
        subscriberId: data.subscriber.id,
        subscription: data.subscriber.subscription,
        monthlyFee: data.subscriber.subscription.monthly_fee,
        co2PerMonth: data.subscriber.subscription.co2_tons_per_month,
        hasSubscription: data.subscriber.has_subscription,
        buttonType: "Edit",
        open: true,
      });
    } else {
      this.setState({
        firstName: data.subscriber.first_name,
        lastName: data.subscriber.last_name,
        email: data.subscriber.email,
        co2PerYear: data.subscriber.co2_tons_per_year,
        subscriberId: data.subscriber.id,
        buttonType: "Edit",
        open: true,
      });
    }
  }

  handleViewOpen(data) {
    console.log(data.subscriber.subscription);
    this.setState({
      firstName: data.subscriber.first_name,
      lastName: data.subscriber.last_name,
      email: data.subscriber.email,
      co2PerYear: data.subscriber.co2_tons_per_year,
      subscription: data.subscriber.subscription,
      viewOpen: true,
    });
  }

  render() {
    const DialogTitle = withStyles(styles)((props) => {
      const { children, classes, onClose, ...other } = props;
      return (
        <MuiDialogTitle disableTypography className={classes.root} {...other}>
          <Typography variant="h6">{children}</Typography>
          {onClose ? (
            <IconButton
              aria-label="close"
              className={classes.closeButton}
              onClick={onClose}
            >
              <CloseIcon />
            </IconButton>
          ) : null}
        </MuiDialogTitle>
      );
    });

    const DialogContent = withStyles((theme) => ({
      viewRoot: {
        padding: theme.spacing(2),
      },
    }))(MuiDialogContent);

    const { classes } = this.props;
    const { open, errors, viewOpen } = this.state;

    const handleClickOpen = () => {
      this.setState({
        suscriberId: "",
        firstName: "",
        lastName: "",
        buttonType: "",
        open: true,
      });
    };

    const handleSubmit = (event) => {
      authMiddleWare(this.props.history);
      event.preventDefault();
      console.log(this.state.hasSubscription);
      const subscriber = {
        first_name: this.state.firstName,
        last_name: this.state.lastName,
        email: this.state.email,
        co2_tons_per_year: this.state.co2PerYear,
      };
      if (this.state.hasSubscription == true) {
        subscriber.has_subscription = this.state.hasSubscription;
        subscriber.subscription = {
          monthly_fee: this.state.monthlyFee,
          co2_tons_per_month: this.state.co2PerMonth,
        };
      }
      let options = {};
      if (this.state.buttonType === "Edit") {
        options = {
          url: `/api/v1/subscribers/${this.state.subscriberId}/`,
          method: "patch",
          data: subscriber,
        };
      } else {
        options = {
          url: "/api/v1/subscribers/new/",
          method: "post",
          data: subscriber,
        };
      }
      const token = localStorage.getItem("token");
      axios.defaults.headers.common = { Authorization: `${token}` };
      axios(options)
        .then(() => {
          this.setState({ open: false });
          window.location.reload();
        })
        .catch((error) => {
          this.setState({ open: true, errors: error.response.data });
          console.log(error);
        });
    };

    const handleViewClose = () => {
      this.setState({ viewOpen: false });
    };

    const handleClose = (event) => {
      this.setState({ open: false });
    };

    if (this.state.uiLoading === true) {
      return (
        <main className={classes.content}>
          <div className={classes.toolbar} />
          {this.state.uiLoading && (
            <CircularProgress size={150} className={classes.uiProgess} />
          )}
        </main>
      );
    } else {
      return (
        <main className={classes.content}>
          <div className={classes.toolbar} />

          <IconButton
            className={classes.floatingButton}
            color="primary"
            aria-label="Add Subscriber"
            onClick={handleClickOpen}
          >
            <AddCircleIcon style={{ fontSize: 60 }} />
          </IconButton>
          <Dialog
            fullScreen
            open={open}
            onClose={handleClose}
            TransitionComponent={Transition}
          >
            <AppBar className={classes.appBar}>
              <Toolbar>
                <IconButton
                  edge="start"
                  color="inherit"
                  onClick={handleClose}
                  aria-label="close"
                >
                  <CloseIcon />
                </IconButton>
                <Typography variant="h6" className={classes.name}>
                  {this.state.buttonType === "Edit"
                    ? "Edit subscriber"
                    : "Create new subscriber"}
                </Typography>
                <Button
                  autoFocus
                  color="inherit"
                  onClick={handleSubmit}
                  className={classes.submitButton}
                >
                  {this.state.buttonType === "Edit" ? "Save" : "Create"}
                </Button>
              </Toolbar>
            </AppBar>

            <form className={classes.form} noValidate>
              <div className={classes.toolbar}></div>
              <Grid container spacing={2}>
                <Grid item xs={6}>
                  <TextField
                    variant="outlined"
                    required
                    fullWidth
                    id="subscriberFirstName"
                    label="First Name"
                    name="firstName"
                    autoComplete="subscriberFirstName"
                    helperText={errors.firstName}
                    value={this.state.firstName}
                    error={errors.name ? true : false}
                    onChange={this.handleChange}
                  />
                </Grid>
                <Grid item xs={6}>
                  <TextField
                    variant="outlined"
                    required
                    fullWidth
                    id="subscriberLastName"
                    label="Last Name"
                    name="lastName"
                    autoComplete="subscriberLastName"
                    helperText={errors.lastName}
                    value={this.state.lastName}
                    error={errors.lastName ? true : false}
                    onChange={this.handleChange}
                  />
                </Grid>
                <Grid item xs={6}>
                  <TextField
                    variant="outlined"
                    required
                    fullWidth
                    label="Email"
                    name="email"
                    value={this.state.email}
                    onChange={this.handleChange}
                  />
                </Grid>
                <Grid item xs={6}>
                  <TextField
                    variant="outlined"
                    required
                    fullWidth
                    id="subscriberCo2PerYear"
                    label="Co2 tons per year"
                    name="co2PerYear"
                    helperText={errors.co2PerYear}
                    value={this.state.co2PerYear}
                    error={errors.co2PerYear ? true : false}
                    onChange={this.handleChange}
                  />
                </Grid>
                <div></div>
                <Grid
                  item
                  xs={12}
                  hidden={this.state.hasSubscription == false ? true : false}
                >
                  <Typography component="h4" className={classes.name}>
                    Subscription Details
                  </Typography>
                </Grid>
                <Grid
                  item
                  xs={6}
                  hidden={this.state.hasSubscription == false ? true : false}
                >
                  <TextField
                    variant="outlined"
                    required
                    fullWidth
                    id="monthlyFee"
                    label="Monthly fee"
                    name="monthlyFee"
                    helperText={errors.monthlyFee}
                    value={this.state.monthlyFee}
                    error={errors.monthlyFee ? true : false}
                    onChange={this.handleChange}
                  />
                </Grid>
                <Grid
                  item
                  xs={6}
                  hidden={this.state.hasSubscription == false ? true : false}
                >
                  <TextField
                    variant="outlined"
                    required
                    fullWidth
                    id="co2PerMonth"
                    label="co2 tons per month"
                    name="co2PerMonth"
                    helperText={errors.co2PerMonth}
                    value={this.state.co2PerMonth}
                    error={errors.co2PerMonth ? true : false}
                    onChange={this.handleChange}
                  />
                </Grid>
              </Grid>
            </form>
          </Dialog>

          <Grid container spacing={2}>
            {this.state.subscribers.map((subscriber) => (
              <Grid item xs={12} sm={6}>
                <Card className={classes.root} variant="outlined">
                  <CardContent>
                    <Typography component="h4">
                      {subscriber.first_name} {subscriber.last_name}
                    </Typography>
                    <Typography className={classes.pos} color="textSecondary">
                      {subscriber.email}
                    </Typography>
                  </CardContent>
                  <CardActions>
                    <Button
                      size="small"
                      color="primary"
                      onClick={() => this.handleViewOpen({ subscriber })}
                    >
                      {" "}
                      View{" "}
                    </Button>
                    <Button
                      size="small"
                      color="primary"
                      onClick={() => this.handleEditClickOpen({ subscriber })}
                    >
                      Edit
                    </Button>
                    <Button
                      size="small"
                      color="primary"
                      onClick={() => this.deleteTodoHandler({ subscriber })}
                    >
                      Delete
                    </Button>
                    <Button
                      disabled={
                        subscriber.has_subscription == false ? false : true
                      }
                      size="small"
                      color="primary"
                      onClick={() =>
                        this.createSubscribeHandler({ subscriber })
                      }
                    >
                      {subscriber.has_subscription == false
                        ? "Add subscription"
                        : null}
                    </Button>
                  </CardActions>
                </Card>
              </Grid>
            ))}
          </Grid>

          <Dialog
            onClose={handleViewClose}
            aria-labelledby="customized-dialog-name"
            open={viewOpen}
            fullWidth
            classes={{ paperFullWidth: classes.dialogeStyle }}
          >
            <DialogTitle id="customized-dialog-name" onClose={handleViewClose}>
              {this.state.firstName} {this.state.lastName}
            </DialogTitle>
            <DialogContent dividers>
              <Typography component="h6" color="textSecondary">
                Email
              </Typography>
              <Typography component="h4">{this.state.email}</Typography>
              <Typography component="h6" color="textSecondary">
                Carbon Footprint
              </Typography>
              <Typography component="h4">
                {this.state.co2PerYear} CO2 tons/year
              </Typography>
              <Typography component="h4">
                {this.state.subscription != null
                  ? this.state.subscription.co2_tons_per_month +
                    " CO2 tons/month"
                  : ""}
              </Typography>
              <Typography component="h6" color="textSecondary">
                {this.state.subscription != null
                  ? "Monthly fee (USD + Taxes)"
                  : ""}
              </Typography>
              <Typography component="h4">
                {this.state.subscription != null
                  ? "$ " + this.state.subscription.monthly_fee
                  : ""}
              </Typography>
            </DialogContent>
          </Dialog>
        </main>
      );
    }
  }
}

export default withStyles(styles)(subscriber);
