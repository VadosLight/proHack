from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = 'polls'
    def ready(self):
         global modelR
        modelR = load_model(os.path.join(os.getcwd(),"model_best_weights.h5"))
        print("init Model")
        