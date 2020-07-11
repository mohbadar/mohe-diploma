package af.asr.mohediploma;

import af.asr.mohediploma.repository.CertificateRepository;
import af.asr.mohediploma.service.ExecutionService;
import af.asr.mohediploma.service.JasperService;
import net.sf.jasperreports.engine.JRException;
import net.sf.jasperreports.engine.JasperPrint;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import java.util.HashMap;
import java.util.Map;

@SpringBootApplication
public class Application {

	private static ExecutionService executionService;

	@Autowired
	public Application(ExecutionService executionService){
		this.executionService = executionService;
	}

	public static void main(String[] args) throws JRException {
		SpringApplication.run(Application.class, args);
		new Application(executionService).execute();
	}

	private void execute() throws JRException {
		executionService.execute();
	}

}
