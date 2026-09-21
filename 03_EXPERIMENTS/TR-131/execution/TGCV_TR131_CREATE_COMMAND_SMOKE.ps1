# TGCV TR-131 — Rainbow direct-command infrastructure smoke-test generator
# Scientific execution remains NOT AUTHORIZED.
# This script only generates the local Java harness; it does not execute a scientific A/B experiment.

$java = @'
import org.sa.rainbow.core.models.ModelsManager;
import org.sa.rainbow.core.models.ModelReference;
import org.sa.rainbow.model.acme.AcmeModelInstance;
import org.sa.rainbow.model.acme.swim.commands.SwimCommandFactory;
import org.sa.rainbow.model.acme.swim.commands.SetDimmerCmd;
import org.acmestudio.acme.element.IAcmeComponent;

public class CommandSmoke {
    public static void main(String[] args) throws Exception {
        System.setProperty("rainbow.target", "swim");
        ModelsManager models = new ModelsManager();
        models.initializeModels();
        AcmeModelInstance model = (AcmeModelInstance) models.getModelInstance(
            new ModelReference("SwimSys", "Acme")
        );
        IAcmeComponent lb0 = model.resolveInModel("LB0", IAcmeComponent.class);
        System.out.println("LB0=" + lb0);
        System.out.println("DIMMER=" + model.getProperty("/self/components:LB0.dimmer"));
        SwimCommandFactory factory = (SwimCommandFactory) model.getCommandFactory();
        SetDimmerCmd command = factory.setDimmerCmd(lb0, 0.5);
        System.out.println("COMMAND=" + command);
        System.out.println("CAN_EXECUTE=" + command.canExecute());
    }
}

'@

$javaPath = Join-Path $PSScriptRoot "CommandSmoke.java"
[System.IO.File]::WriteAllText($javaPath, $java, (New-Object System.Text.UTF8Encoding($false)))
Write-Host "CREATED=$javaPath"
