from tensorboardX import SummaryWriter
from comet_ml import Experiment

class NullLogger:

    def __init__(self):
        pass

    @property
    def run_name(self):
        return "Null"

    def meta(self, *args, **kwargs):
        pass

    def log(self, name, loss, step):
        pass


class TensorboardX:

    def __init__(self, logdir, run_name):
        self._logdir = logdir
        self._writer = SummaryWriter(logdir=logdir)
        self.run_name = run_name

    def args(self, arg_text):
        self._writer.add_text("args", arg_text)

    def meta(self, params):
        self._writer.add_hparams(hparam_dict=params, metric_dict={})

    def log(self, name, value, step):
        self._writer.add_scalar(name, value, step)


class CometML:

    def __init__(self, api_key, project_name, workspace, debug=True):
        self._exp = Experiment(
            api_key=api_key,
            project_name=project_name,
            workspace=workspace,
            disabled=debug,
        )
        if not (self._exp.alive or debug):
            raise RuntimeError("Cannot connect to Comet ML")
        self._exp.disable_mp()

    @property
    def run_name(self):
        return self._exp.get_key()

    def args(self, arg_text):
        self._exp.log_parameter("cmd args", arg_text)

    def meta(self, params):
        self._exp.log_parameters(params)

    def log(self, name, value, step):
        self._exp.log_metric(
            name=name,
            value=value,
            step=step,
        )


class WanDB:

    def __init__(self):
        pass

    @property
    def run_name(self):
        return "Null"

    def meta(self, *args, **kwargs):
        pass

    def log(self, name, value, step):
        pass
