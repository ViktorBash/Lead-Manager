// Root reducer is meeting place for all of the reducers
import {combineReducers} from "redux";
import leads from "./leads";
import errors from "./errors";
import messages from "./messages";
import auth from "./auth";

export default combineReducers({
    leads,
    errors,
    messages,
    auth
});