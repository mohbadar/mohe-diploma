/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package af.asr.mohediploma.model;

import java.io.Serializable;
import java.util.List;
import javax.persistence.Basic;
import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.OneToMany;
import javax.persistence.Table;

/**
 *
 * @author badar
 */
@Entity
@Table(name = "generic_university")
//@NamedQueries({
//    @NamedQuery(name = "GenericUniversity.findAll", query = "SELECT g FROM GenericUniversity g")})
public class University implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Basic(optional = false)
    @Column(name = "id")
    private Integer id;
    @Basic(optional = false)
    @Column(name = "name")
    private String name;
    @Basic(optional = false)
    @Column(name = "code")
    private String code;
    @Basic(optional = false)
    @Column(name = "province")
    private String province;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "universityId")
    private List<Blankdiploma> blankdiplomaList;
    @JoinColumn(name = "user_id", referencedColumnName = "id")
    @ManyToOne
    private AuthUser userId;
    @OneToMany(mappedBy = "universityId")
    private List<Faculty> facultyList;
    @OneToMany(mappedBy = "universityId")
    private List<Userfacultyrelation> userfacultyrelationList;
    @OneToMany(mappedBy = "universityId")
    private List<Department> genericDepartmentList;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "universityId")
    private List<Universitydiplomadistribution> universitydiplomadistributionList;
    @OneToMany(mappedBy = "universityId")
    private List<Diploma> diplomaList;

    public University() {
    }

    public University(Integer id) {
        this.id = id;
    }

    public University(Integer id, String name, String code, String province) {
        this.id = id;
        this.name = name;
        this.code = code;
        this.province = province;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getProvince() {
        return province;
    }

    public void setProvince(String province) {
        this.province = province;
    }

    public List<Blankdiploma> getBlankdiplomaList() {
        return blankdiplomaList;
    }

    public void setBlankdiplomaList(List<Blankdiploma> blankdiplomaList) {
        this.blankdiplomaList = blankdiplomaList;
    }

    public AuthUser getUserId() {
        return userId;
    }

    public void setUserId(AuthUser userId) {
        this.userId = userId;
    }

    public List<Faculty> getFacultyList() {
        return facultyList;
    }

    public void setFacultyList(List<Faculty> facultyList) {
        this.facultyList = facultyList;
    }

    public List<Userfacultyrelation> getUserfacultyrelationList() {
        return userfacultyrelationList;
    }

    public void setUserfacultyrelationList(List<Userfacultyrelation> userfacultyrelationList) {
        this.userfacultyrelationList = userfacultyrelationList;
    }

    public List<Department> getGenericDepartmentList() {
        return genericDepartmentList;
    }

    public void setGenericDepartmentList(List<Department> genericDepartmentList) {
        this.genericDepartmentList = genericDepartmentList;
    }

    public List<Universitydiplomadistribution> getUniversitydiplomadistributionList() {
        return universitydiplomadistributionList;
    }

    public void setUniversitydiplomadistributionList(List<Universitydiplomadistribution> universitydiplomadistributionList) {
        this.universitydiplomadistributionList = universitydiplomadistributionList;
    }

    public List<Diploma> getDiplomaList() {
        return diplomaList;
    }

    public void setDiplomaList(List<Diploma> diplomaList) {
        this.diplomaList = diplomaList;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (id != null ? id.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof University)) {
            return false;
        }
        University other = (University) object;
        if ((this.id == null && other.id != null) || (this.id != null && !this.id.equals(other.id))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "af.asr.mohediploma.model.GenericUniversity[ id=" + id + " ]";
    }
    
}
