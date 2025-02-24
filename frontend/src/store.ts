import { createStore } from 'redux';

interface AppState {
  projectArea: any;
  modelResults: any;
}

const initialState: AppState = {
  projectArea: null,
  modelResults: null,
};

function rootReducer(state = initialState, action: any) {
  switch (action.type) {
    case 'SET_PROJECT_AREA':
      return { ...state, projectArea: action.payload };
    case 'SET_MODEL_RESULTS':
      return { ...state, modelResults: action.payload };
    default:
      return state;
  }
}

const store = createStore(rootReducer);
export default store;