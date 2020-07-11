package af.asr.mohediploma.service;

import af.asr.mohediploma.repository.CertificateRepository;
import net.sf.jasperreports.engine.JRException;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.Map;

@Service
public class ExecutionService {

    private final CertificateRepository certificateRepository;
    private final JasperService jasperService;
    private final String JASPER_FILE_PATH ="C:\\Users\\badar\\diploma.jrxml";
    private final String OUTFILE_PATH = "C:\\Users\\badar\\diploma.pdf";

    public ExecutionService(CertificateRepository certificateRepository, JasperService jasperService) {
        this.certificateRepository = certificateRepository;
        this.jasperService = jasperService;
    }

    public void execute() throws JRException {

        for (int i=0; i< 4; i++)
        {
            Map<String, Object> params = new HashMap<>();
            params.put("firstname", "Badar" + i);
            params.put("lastname", "Hashimi");
            params.put("fathername", "Mohammad");
            params.put("dob", "2020/23/32");
            params.put("test", "test");

            jasperService.printDiploma(params, JASPER_FILE_PATH, certificateRepository.findAll(), "jasper_"+i+"_.pdf");
        }


    }
}
