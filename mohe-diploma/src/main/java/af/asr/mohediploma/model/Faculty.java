/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package af.asr.mohediploma.model;

import java.io.Serializable;
import java.util.List;
import javax.persistence.Basic;
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
@Table(name = "generic_faculty")
//@NamedQueries({
//    @NamedQuery(name = "GenericFaculty.findAll", query = "SELECT g FROM GenericFaculty g")})
public class Faculty implements Serializable {

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
    @JoinColumn(name = "user_id", referencedColumnName = "id")
    @ManyToOne
    private AuthUser userId;
    @JoinColumn(name = "university_id", referencedColumnName = "id")
    @ManyToOne
    private University universityId;
    @OneToMany(mappedBy = "facultyId")
    private List<Userfacultyrelation> userfacultyrelationList;
    @OneToMany(mappedBy = "facultyId")
    private List<Department> genericDepartmentList;

    public Faculty() {
    }

    public Faculty(Integer id) {
        this.id = id;
    }

    public Faculty(Integer id, String name, String code) {
        this.id = id;
        this.name = name;
        this.code = code;
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

    public AuthUser getUserId() {
        return userId;
    }

    public void setUserId(AuthUser userId) {
        this.userId = userId;
    }

    public University getUniversityId() {
        return universityId;
    }

    public void setUniversityId(University universityId) {
        this.universityId = universityId;
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

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (id != null ? id.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof Faculty)) {
            return false;
        }
        Faculty other = (Faculty) object;
        if ((this.id == null && other.id != null) || (this.id != null && !this.id.equals(other.id))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "af.asr.mohediploma.model.GenericFaculty[ id=" + id + " ]";
    }
    
}
